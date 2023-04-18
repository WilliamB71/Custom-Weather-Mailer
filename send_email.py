import smtplib
import arrow
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from beach_image import Image
from html_template import Email_Content


class SendEmail:
    def send(send_list):
        timezone = 'Europe/London'
        Image.update()

        # create email message
        for recipent in send_list:

            msg = MIMEMultipart()
            msg['Subject'] = f'Bodley Weather Report {arrow.now(tz=timezone).format("DD-MM")}'
            msg['From'] = 'canfordcliffsforecast@gmail.com'
            msg['To'] = str(recipent)
            msg.attach(MIMEText(Email_Content.write(), 'html'))
            with open('/tmp/Beach_Image.png', 'rb') as f:
                image = MIMEImage(f.read())
                msg.attach(image)
            image.add_header('Content-ID', '<Beach_Image.png>')
            

            # send email
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587
            smtp_username = 'canfordcliffsforecast@gmail.com'
            smtp_password = 'drdnekpfwcxcxsbk'
            smtp_conn = smtplib.SMTP(smtp_server, smtp_port)
            smtp_conn.starttls()
            smtp_conn.login(smtp_username, smtp_password)
            smtp_conn.sendmail('canfordcliffsforecast@gmail.com',
                               str(recipent), msg.as_string())
            smtp_conn.quit()
