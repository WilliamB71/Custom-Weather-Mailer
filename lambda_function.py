import json
from send_email import SendEmail
        
def lambda_handler(event, context):
    mail_list = ['williambloomfield71@hotmail.co.uk', ]
    SendEmail.send(mail_list)
    return "email sent"


lambda_handler(event=None, context=None)