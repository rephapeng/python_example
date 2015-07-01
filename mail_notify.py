#!/usr/bin/python

#encoding: utf-8

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from email.header import Header
import sys
import smtplib
#---------------------------------------------------
#---------------------------------------------------

def send_mail(message):
	strFrom = 'sender@domain.com'
	strTo = 'receiver@domain.com'
	smtp_server = 'smtp.googlemail.com:587'
	smtp_pass = '123456789'
#	if sys.argv[1]!="master" and sys.argv[1]!="backup" and sys.argv[1]!="fault" :
#		sys.exit()
#	else :
#		notify_type=sys.argv[1]

	mail_title ='Message from failover'
	mail_body_plain=message

	mail_body_html='<b><font color=red>'+message+'</font></b>'
	msgRoot = MIMEMultipart('releated')
	msgRoot['Subject'] = Header(mail_title,'utf-8')
	msgRoot['From'] = strFrom
	msgRoot['To'] = strTo

	msgAlternative = MIMEMultipart('alternative')
	msgRoot.attach(msgAlternative)

	msgText = MIMEText(mail_body_html, 'plain', 'utf-8')
	msgAlternative.attach(msgText)

	msgText = MIMEText(mail_body_html, 'html', 'utf-8')
	msgAlternative.attach(msgText)

	smtp = smtplib.SMTP()

	smtp.connect(smtp_server)
	smtp.ehlo()
	smtp.starttls()
	smtp.ehlo()
	smtp.login(strFrom,smtp_pass)
	smtp.sendmail(strFrom, strTo, msgRoot.as_string())
	smtp.quit()
