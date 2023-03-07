import arrow
from send_email import SendEmail
import time

mail_list = ['williambloomfield71@hotmail.co.uk', 'rob@jwbservices.co.uk']

while True:
    timezone = "Europe/London"
    now = arrow.now(tz=timezone).time().strftime("%H:%M:%S")
    if now == "07:00:00":
        SendEmail.send(mail_list)
        time.sleep(5)
        
