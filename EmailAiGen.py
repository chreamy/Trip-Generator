import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import bestairport
import json
import textgen
import image
import mailformat

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
def gencontent(data,theme):
    locs = [data['places'][i]['name'] for i in range(3)]
    imgs = list([image.getimage(i) for i in locs])
    out = {'imgs':[],'descs':[]}
    text = str(textgen.gen(data['city'].lower().title(), theme, locs))
    img, imgs = image.usebestratio(imgs[0],2)
    out['imgs'].append(img)
    out['descs'].append(text)
    return out



def send(name, theme, loc,date, message=message):
    message["Subject"] = f"Personalized {theme} Trip For {name}"
    data = bestairport.getplaces(25, theme, loc ,date)
    outfile = open(f"data.json", "w")
    json.dump(data, outfile, sort_keys=True, indent=4)
    outfile.close()

   #out = open('imgs.txt','w')
    #out.write(str(imgs))
    #out.close()
    content=gencontent(data,theme)
    #plain = MIMEText(f"""{text.strip()}""", "plain")
    #out = open('a.html', 'w')
    #out.write(html)
    #out.close()

    #message.attach(plain)
    part = MIMEText(mailformat.gethtml(content), 'html')
    message.attach(part)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
            )
#html = mailformat.gethtml()
send('Chris','Music Venues', 'IAH', '2023-02-15')

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