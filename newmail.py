# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib 

# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 

# start TLS for security 
s.starttls() 

# Authentication 
s.login("shivamguptasg1808@gmail.com", "*****") 

# message to be sent 
message = "BUILD/TEST FAILED"

# sending the mail 
s.sendmail("shivamguptasg1808@gmail.com", "shivamguptasparklev@gmail.com", message) 

# terminating the session 
s.quit() 

