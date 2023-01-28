import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

sender_email = "testrunpython@gmail.com"
receiver_email = "testrunpython@gmail.com"  # chrislinkou
password = 'esxnhmhgcqpxrsxb'

message = MIMEMultipart("alternative")
message["From"] = sender_email
message["To"] = receiver_email

def events(name,interest,message=message):
    text = f"""
            Hi {name},\n
            Thanks for signing up to PLACEHOLDER!\n
            Our job is to ensure you get to go to the best {event} easily. No more hours wasted deciding on the best venue,
            or researching the cheapest flights, or debating whether it's even worth the trip!
            So why don't you go take a break? Take a minute to appreciate all the time (and money) you're about to save.
            To make sure you feel extra relaxed we've included a little special something just for you...\n
            Use Discount Code: Welcome10 for 10% off your first purchase (and that's on top of our other deals!)"""
    html = f"""
            <html>
                <body>
                    <p><h4>Hi, {name}</h4>
                    Thanks for signing up to PLACEHOLDER!<br>
                    Our job is to ensure you get to go to <strong><em>the best</em></strong> {event} easily. No more hours 
                    wasted<br>deciding on the best venue, or researching the cheapest flights, or debating whether it's 
                    even worth the trip!<br>So why don't you go take a break? Take a minute to appreciate all the time 
                    <i>(and money)</i> you're about to save.<br>To make sure you feel extra relaxed we've included a 
                    little special something just for you...<h2>Use Discount Code: <h1>Welcome10</h1> for <strong>10% off your 
                    first purchase</strong><h2> <i>(and that's on top of our other deals!)</i><br>
                    </p>
                </body>
            </html>
            """
    message = [text, html]
    return message
def welcome(name, interest, message=message):
    message["Subject"] = "Welcome to PLACEHOLDER!"
    if interest == 'music':
        event = 'concerts'
        image = 'concert.png'
    elif interest == 'sports':
        event = 'games'
        image = 'sports.png'
    else:
        event = 'events'
    text = f"""
            Hi {name},\n
            Thanks for signing up to PLACEHOLDER!\n
            Our job is to ensure you get to go to the best {event} easily. No more hours wasted deciding on the best venue,
            or researching the cheapest flights, or debating whether it's even worth the trip!
            So why don't you go take a break? Take a minute to appreciate all the time (and money) you're about to save.
            To make sure you feel extra relaxed we've included a little special something just for you...\n
            Use Discount Code: Welcome10 for 10% off your first purchase (and that's on top of our other deals!)"""
    html = f"""
            <html>
                <head>
                </head>
                <body>
                    <p><h4>Hi, {name}</h4>
                    Thanks for signing up to PLACEHOLDER!<br>
                    Our job is to ensure you get to go to <strong><em>the best</em></strong> {event} easily. No more hours 
                    wasted<br>deciding on the best venue, or researching the cheapest flights, or debating whether it's 
                    even worth the trip!<br>So why don't you go take a break? Take a minute to appreciate all the time 
                    <i>(and money)</i> you're about to save.<br>To make sure you feel extra relaxed we've included a 
                    little special something just for you...<h2>Use Discount Code: <h1>Welcome10</h1> for <strong>10% off your 
                    first purchase</strong><h2> <i>(and that's on top of our other deals!)</i><br>
                    <img src="cid:{image}"
                    </p>
                </body>
            </html>
            """
    message = [text,html]
    return  message
def test(message=message):
    message["Subject"] = "Multipart Test"
    text = """\
        Hi,\n
        This is a test!\n
        Does it look okay?"""
    html = """\
        <html>
          <body>
            <p>Hi,<br>
               This is a test!<br>
               Does it look okay?
            </p>
          </body>
        </html>
        """
    message = [text,html]
    return message
def send(email, message=message):
    if email == 'welcome':
        mess = welcome()
    elif email == 'concert':
        mess = concert()
    elif email == 'test':
        mess = test()
    plain = MIMEText(mess[0], "plain")
    html = MIMEText(mess[1], "html")
    message.attach(plain)
    message.attach(html)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
            )
print(welcome('Rebecca', 'music')[2])