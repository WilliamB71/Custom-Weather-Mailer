import requests
from utils import unix_to_dt, increment_day_dt, temp_desc, weather_desc, wind_desc
import arrow


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

        three_day_forecast = {arrow.now().format('DD-MM'): [],
                              arrow.now().shift(days=1).format('DD-MM'): [], arrow.now().shift(days=2).format('DD-MM'): []}
        formatted_forecast = {date: {} for date in three_day_forecast}

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

    def html_table():
        weather_dict = Weather.report()
        table = "<table style='border-collapse: collapse; width: 80%; margin: auto; font-family: sans-serif;'>"
        table += "<tr style='background-color: #0099cc; color: white; text-align: center;'><th style='padding: 10px;'>Day</th><th style='padding: 10px;'>Temperature</th><th style='padding: 10px;'>Weather Description</th><th style='padding: 10px;'>Wind Speed</th></tr>"
        for day, weather in weather_dict.items():
            temp = weather.get('Temperature', '')
            weather_desc = "<br>".join(weather.get('Weather Description', []))
            wind_speed = weather.get('Wind Speed', '')
            table += f"<tr style='text-align: center;'><td style='padding: 10px; background-color: #f2f2f2;'>{day.title()}</td><td style='padding: 10px;'>{temp}</td><td style='padding: 10px; text-align: left;'>{weather_desc}</td><td style='padding: 10px;'>{wind_speed}</td></tr>"
        table += "</table>"
        return table
