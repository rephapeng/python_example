#!/usr/bin/python

import smtplib
import netifaces
import sys

#send mail menggunakan mail relay

ip = netifaces.ifaddresses("eth0")[netifaces.AF_INET][0]['addr']

if sys.argv[1]!="master" and sys.argv[1]!="backup" and sys.argv[1]!="fault" :
    sys.exit()
else :
    notify_type=sys.argv[1]

sender = 'sender@sender.com'
receivers = ['recievers@recievers.com']

message = """From: from<%s>
To: To <%s>
Subject: send mail using mail relay 

this is message

""" %(sender, receivers, ip, notify_type)

try:
    smtpObj = smtplib.SMTP('smtp-host:25')
    smtpObj.sendmail(sender, receivers, message)         
    print "Successfully sent email"
except SMTPException:
    print "Error: unable to send email"
