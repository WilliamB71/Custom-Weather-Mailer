import requests
import datetime
from utils import unix_to_dt, time_from_dt, increment_day_dt

now = datetime.datetime.now()

API_key = 'f4c16045c21419f2605536881085186b'
lat = '50.703'
lon = '-1.923'
URL = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_key}'

data = requests.get(URL).json()


weather_raw = data['list']
sunrise = unix_to_dt(data['city']['sunrise'])
sunset = unix_to_dt(data['city']['sunset'])

sunrise_dts = {i: increment_day_dt(sunrise, days=i) for i in range(3)}
sunset_dts = {i: increment_day_dt(sunset, days=i) for i in range(3)}

three_day_forecast = {'today': [], 'tomorrow': [], 'day_after_tomorrow': []}

for int_key in sunrise_dts:
    for forecast in weather_raw:
        if sunrise_dts[int_key] <= unix_to_dt(forecast['dt']) <= sunset_dts[int_key]:
            three_day_forecast[list(three_day_forecast.keys())[
                int_key]].append(forecast)

print(three_day_forecast)
