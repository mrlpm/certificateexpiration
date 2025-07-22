#!/bin/env python
from __future__ import print_function
import ssl
import OpenSSL
import datetime

import smtplib
from email.message import EmailMessage
from email.headerregistry import Address
from email.utils import make_msgid

def sendmail(content):
    # Create the base text message.
    msg = EmailMessage()
    msg['Subject'] = "Remider of SSL"
    msg['From'] = Address("Admin Subject", "admin@domain.ltd")
    msg['To'] = (Address("Admin Subject", "admin@domain.ltd"),
                 Address("sysadmin", "user@domain.ltd"))
    msg.set_content(content)
    with smtplib.SMTP('localhost') as s:
        s.send_message(msg)


def check():
    hostname = "mail.domain.ltd"
    port = 443

    num_days = 7
    cert = ssl.get_server_certificate(
        (hostname, port), ssl_version=ssl.PROTOCOL_TLSv1)
    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
    expiry_date = x509.get_notAfter()
    print(str(expiry_date))
    assert expiry_date, "Cert doesn't have an expiry date."

    ssl_date_fmt = r'%Y%m%d%H%M%SZ'
    expires = datetime.datetime.strptime(str(expiry_date)[2:-1], ssl_date_fmt)
    remaining = (expires - datetime.datetime.utcnow()).days

    if remaining <= num_days:
        body = "ALERTING!"
        sendmail(body)
    else:
        print("Not alerting. You have " + str(remaining) + " days") 

if '__main__' == __name__:
    check()
