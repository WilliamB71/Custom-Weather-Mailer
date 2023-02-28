import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

# dictionary with weather parameters
weather_dict = {'28-02': {'Temperature': '7.7°C - 7.7°C', 'Weather Description': ['15:00: light rain'], 'Wind Speed': '15.1 mph - 15.1 mph'}, '01-03': {'Temperature': '5.3°C - 6.9°C', 'Weather Description': ['09:00: broken clouds', '12:00: overcast clouds', '15:00: overcast clouds'], 'Wind Speed': '12.9 mph - 13.6 mph'}, '2023-03-02 13:15:47+00:00': {'Temperature': '3.8°C - 8.8°C', 'Weather Description': ['09:00: few clouds', '12:00: clear sky', '15:00: clear sky'], 'Wind Speed': '10.1 mph - 12.2 mph'}}


def weather_to_html_table(weather_dict):
    table = "<table style='border-collapse: collapse; width: 50%; margin: auto;'>"
    table += "<tr style='background-color: #0099cc; color: white; text-align: center;'><th style='padding: 10px;'>Day</th><th style='padding: 10px;'>Temperature</th><th style='padding: 10px;'>Weather Description</th><th style='padding: 10px;'>Wind Speed</th></tr>"

    for day, weather in weather_dict.items():
        temp = weather.get('Temperature', '')
        weather_desc = "<br>".join(weather.get('Weather Description', []))
        wind_speed = weather.get('Wind Speed', '')

        table += f"<tr style='text-align: center;'><td style='padding: 10px; background-color: #f2f2f2;'>{day.title()}</td><td style='padding: 10px;'>{temp}</td><td style='padding: 10px; text-align: left;'>{weather_desc}</td><td style='padding: 10px;'>{wind_speed}</td></tr>"

    table += "</table>"

    return table


html_table = weather_to_html_table(weather_dict)

print(html_table)


# create email message
msg = MIMEMultipart()
msg['Subject'] = 'Weather Report 5'
msg['From'] = 'canfordcliffsforecast@gmail.com'
msg['To'] = 'williambloomfield71@hotmail.co.uk'
msg.attach(MIMEText(html_table, 'html'))
with open('Beach_Image.png', 'rb') as f:
    bournemouth_image = MIMEImage(f.read())
    bournemouth_image.add_header('Content-Disposition', 'attachment', filename="Bournemouth_Pier.png")
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
                   'williambloomfield71@hotmail.co.uk', msg.as_string())
smtp_conn.quit()
