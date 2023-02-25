from beach_image import Image
from wave_forecast import OceanWeather
from weather_forecast import Weather
from utils import time_from_dt
import smtplib
from email.message import EmailMessage
import os
import pytz
import datetime
import time
gmail_sender = "canfordcliffsforecast@gmail.com"
gmail_password = "drdnekpfwcxcxsbk"

email_recipents = "williambloomfield71@hotmail.co.uk"

# while True:
#     londontz = pytz.timezone("Europe/London")
#     time_ = time_from_dt(datetime.datetime.now(londontz)).strftime("%H:%M:%S")

#     if time_ == "15:44:40":
#         Image.update()
#         weather = Weather.report()
#         surf = OceanWeather.report()

#         print(weather)
#         print(surf)

#         #format/send email


#         time.sleep(5)


from test import table_str
# Create a new email message object
msg = EmailMessage()

# Set the sender, recipients, subject, and body of the email
msg['From'] = gmail_sender
msg['To'] = email_recipents
msg['Subject'] = 'Test email 1'
msg.set_content(table_str)

# Optional: Add a file attachment to the email
with open('Beach_Image.png', 'rb') as f:
    file_data = f.read()
    file_name = os.path.basename(f.name)
msg.add_attachment(file_data, maintype='image', subtype='png', filename=file_name)

# Send the email using an SMTP server
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login(gmail_sender, gmail_password)
    smtp.send_message(msg)
