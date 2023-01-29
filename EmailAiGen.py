import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import bestairport
import json
import textgen
import image
import mailformat
import flight_ticket
import interactive_map
import upload
import time
import math
import event_search

sender_email = "testrunpython@gmail.com"
receiver_email = "chrislinkou@gmail.com"  # chrislinkou
password = 'esxnhmhgcqpxrsxb'

message = MIMEMultipart("alternative")
message["From"] = sender_email
message["To"] = receiver_email

def codetocity(code,data):
    for dat in data:
        print(dat['city'])
        if code in dat:
            return dat['city']
    return 0
def gencontent(data,theme,ticketsc,loc,date):
    locs,dists = [data['places'][i]['name'] for i in range(3)],[data['places'][i]['dist'] for i in range(3)]
    imgs = list([image.getimage(i) for i in locs])
    cityimg = image.getimage(data['city'])
    out = {'imgs':[],'descs':[]}
    out.update({'y':date.split('-')[0],'m':date.split('-')[1],'d':date.split('-')[2],'loc':loc,'des':data['code']})
    text = str(textgen.gen(data['city'].lower().title(), theme, locs))
    img, cityimg = image.usebestratio(cityimg,2)
    out['imgs'].append(img)
    img, imgs[0] = image.usebestratio(imgs[0], 0.5)
    out['imgs'].append(img)
    img, imgs[1] = image.usebestratio(imgs[1], 0.5)
    out['imgs'].append(img)
    img, imgs[2] = image.usebestratio(imgs[2], 0.5)
    out['imgs'].append(img)
    #out['imgs'].append(ticketsc)
    out['imgs'].append(str(interactive_map.create_map(data)))
    out['imgs'].append(str(interactive_map.create_attraction_map(data)))
    img, imgs[0] = image.usebestratio(imgs[0], 1)
    out['imgs'].append(img)
    img, imgs[1] = image.usebestratio(imgs[1], 1.3)
    out['imgs'].append(img)
    img, imgs[2] = image.usebestratio(imgs[2], 1)
    out['imgs'].append(img)

    out['descs'].append(textgen.gentitle(theme))
    out['descs'].append(text)
    t = data['tickets']
    for i in range(3):
        out['descs'].append([t[i]['itineraries'][0]['carrier'],t[i]['price'],t[i]['itineraries'][0]['duration'],t[i]['itineraries'][0]['aircraft'],t[i]['itineraries'][0]['arrive'][2],t[i]['itineraries'][0]['depart'][0],t[i]['itineraries'][0]['arrive'][0]])
    for i in range(3):
        out['descs'].append(textgen.genloc(data['city'].lower().title(),locs[i],math.ceil(dists[i]*0.0019)))
    try:
        out['images'].append(flight_ticket.screenshot(loc,data['city'],date))
    except:
        pass
    out['descs'].append(textgen.temp())
    out['descs'].append(textgen.temp2(data['city'].lower().title()))
    return out



def send(name, theme, loc,date,rad,message=message):
    message["Subject"] = f"Personalized {theme} Trip For {name}"
    data = bestairport.getplaces(rad, theme, loc ,date)
    outfile = open(f"data.json", "w")
    json.dump(data, outfile, sort_keys=True, indent=4)
    outfile.close()
    #ticketsc = flight_ticket.screenshot(loc,data['city'],date)
   #out = open('imgs.txt','w')
    #out.write(str(imgs))
    #out.close()
    ticketsc = ''
    content=gencontent(data,theme,ticketsc,loc,date)
    #plain = MIMEText(f"""{text.strip()}""", "plain")


    #message.attach(plain)
    part = MIMEText(mailformat.gethtml(content), 'html')
    message.attach(part)
    out = open('4.html', 'w')
    out.write(mailformat.gethtml(content))
    out.close()
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
            )
#html = mailformat.gethtml()


def sendtest(message=message):
    message["Subject"] = f""
    part = MIMEText(mailformat.gethtml(), 'html')
    message.attach(part)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
            )
#sendtest()
#name = input('enter name:')
#interest = input('enter interest:')
#location = input('enter location:')
#date = input('enter date:')
send('Chris','Casino', 'IAH', '2023-02-15', 30)
#send(name,interest, location, date)