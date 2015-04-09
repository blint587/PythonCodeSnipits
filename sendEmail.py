# coding=utf-8

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

ss
senderMail = "something@something.com"
recipientMail = "something@something.com"

def mail(mesage):
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Error"
    msg["From"] = senderMail
    msg["To"] = recipientMail

    # Create the body of the message (a plain-text and an HTML version).
    text = "The following ERROR occurred:\n" + mesage
    # html = """\
    # <html>
    #   <head></head>
    #   <body>
    #     <p>Hello!<br>
    #        <br>""" + mesage + """<br>
    #        <br>
    #     </p>
    #   </body>
    # </html>
    # """


    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, "plain")
    # part2 = MIMEText(html, "html")

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    # msg.attach(part2)

    s = smtplib.SMTP("192.168.5.253")
    # sendmail function takes 3 arguments: sender"s address, recipient"s address
    # and message to send - here it is sent as one string.
    s.sendmail(senderMail, recipientMail, msg.as_string())
    s.quit()