import smtplib
import arrow
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from weather_forecast import Weather
from wave_forecast import StormGlass
from beach_image import Image


class SendEmail:
    def send(send_list):
        timezone = 'Europe/London'
        html_table = f"{Weather.html_table()}<br><br>{StormGlass.html_table()}"
        Image.update()

        # create email message
        for recipent in send_list:

            msg = MIMEMultipart()
            msg['Subject'] = f'Bodley Weather Report {arrow.now(tz=timezone).format("DD-MM")}'
            msg['From'] = 'canfordcliffsforecast@gmail.com'
            msg['To'] = str(recipent)
            msg.attach(MIMEText(html_table, 'html'))
            with open('/tmp/Beach_Image.png', 'rb') as f:
                bournemouth_image = MIMEImage(f.read())
                bournemouth_image.add_header(
                    'Content-Disposition', 'attachment', filename="Bournemouth_Pier.png")
                msg.attach(bournemouth_image)

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
