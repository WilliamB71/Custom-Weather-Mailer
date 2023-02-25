import requests
from utils import unix_to_dt, increment_day_dt, temp_desc, weather_desc, wind_desc


class Weather:
    def data():
        API_key = 'f4c16045c21419f2605536881085186b'
        lat = '50.703'
        lon = '-1.923'
        URL = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_key}'

        return requests.get(URL).json()

    def daylight_times():
        data = Weather.data()
        sunrise = unix_to_dt(data['city']['sunrise'])
        sunset = unix_to_dt(data['city']['sunset'])
        return sunrise, sunset

    def report():
        data = Weather.data()
        sunrise, sunset = Weather.daylight_times()
        weather_raw = data['list']

        sunrise_dts = {i: increment_day_dt(sunrise, days=i) for i in range(3)}
        sunset_dts = {i: increment_day_dt(sunset, days=i) for i in range(3)}

        three_day_forecast = {'today': [],
                              'tomorrow': [], 'Day after Tomorrow': []}
        formatted_forecast = {'today': {},
                              'tomorrow': {}, 'Day after Tomorrow': {}}

        for int_key in sunrise_dts:
            for forecast in weather_raw:
                if sunrise_dts[int_key] <= unix_to_dt(forecast['dt']) <= sunset_dts[int_key]:
                    three_day_forecast[list(three_day_forecast.keys())[
                        int_key]].append(forecast)

        for day_key in formatted_forecast:
            if three_day_forecast[day_key]:
                formatted_forecast[day_key]['Temperature'] = temp_desc(
                    three_day_forecast[day_key])
                formatted_forecast[day_key]['Weather Description'] = weather_desc(
                    three_day_forecast[day_key])
                formatted_forecast[day_key]['Wind Speed'] = wind_desc(
                    three_day_forecast[day_key])

        return formatted_forecast
    

# print(Weather.report())