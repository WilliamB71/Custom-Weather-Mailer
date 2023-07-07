import json
from send_email import SendEmail
        
def lambda_handler(event, context):
    mail_list = ['example@email.cpm']
    SendEmail.send(mail_list)
    return "email sent"