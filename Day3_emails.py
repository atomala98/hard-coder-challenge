import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import ssl
import getpass
import re
from validate_email import validate_email

def sendMails():
    sender = input("Email address")
    password = getpass.getpass()
    port = 465
    context = ssl.create_default_context()

    text = """\
    Hi {}! 

    it’s file generated for you"""

    html = """\
    <html>
        <body>
            <p>Hi {}!<br>
            it’s file generated for you<br>
            </p>
        </body>
    </html>
    """

    try:
        excel_data = pd.read_excel(io="emails.xlsx", engine="openpyxl")
    except:
        print("No excel file found!")
        return False

    try:
        img_data = open("image.jpeg", "rb").read()
    except:
        print("No image file found!")
        return False
        
    for id in range(len(excel_data["Email"])):
        if validate_email(email=excel_data["Email"][id]):
            message = MIMEMultipart("alternative")
            message["Subject"] = "Your image"
            message["From"] = sender
            receiver = excel_data["Email"][id]
            message["To"] = receiver
            name = excel_data["Name and surname"][id].split(' ')
            part1 = MIMEText(text, "plain")
            part2 = MIMEText(html.format(name[0]), "html")
            message.attach(part1)
            message.attach(part2)    
            image = MIMEImage(img_data, name = "{}_{}_image.png".format(name[0], name[1]))
            message.attach(image)
            with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                server.login(sender, password)
                server.sendmail(sender, receiver, message.as_string())
            del message
        else:
            print("Email {} is not valid".format(excel_data["Email"][id]))
            
sendMails()