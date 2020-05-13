#!/usr/bin/python

import smtplib

sender = 'shivamguptasg1808@gmai.com'
receivers = ['shivamguptasg1808@gmai.com']

message = """From: From Person <shivamguptasg1808@gmai.com>
To: To Person <shivamguptasg1808@gmai.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('192.168.0.104')
   smtpObj.sendmail(sender, receivers, message)         
   print ("Successfully sent email")
except SMTPException:
   print ("Error: unable to send email")
