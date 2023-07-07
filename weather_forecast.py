import requests
from utils import unix_to_dt, increment_day_dt, temp_desc, weather_desc, wind_desc, icon_desc
import arrow


class Weather:
    def data():
        API_key = 'examplekey'
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
        ret_dict = {}
        data = Weather.data()
        sunrise, sunset = Weather.daylight_times()
        weather_raw = data['list']

        sunrise_dts = {i: increment_day_dt(sunrise, days=i) for i in range(5)}
        sunset_dts = {i: increment_day_dt(sunset, days=i) for i in range(5)}

        five_day_forecast = {arrow.now().shift(days=i).format('DD-MM'): [] for i in range(0, 5)}

        formatted_forecast = {date: {} for date in five_day_forecast}

        for int_key in sunrise_dts:
            for forecast in weather_raw:
                if sunrise_dts[int_key] <= unix_to_dt(forecast['dt']) <= sunset_dts[int_key]:
                    five_day_forecast[list(five_day_forecast.keys())[
                        int_key]].append(forecast)

        for day_key in formatted_forecast:
            if five_day_forecast[day_key]:
                formatted_forecast[day_key]['Temperature'] = temp_desc(
                    five_day_forecast[day_key])
                formatted_forecast[day_key]['Weather Description'] = weather_desc(
                    five_day_forecast[day_key])
                formatted_forecast[day_key]['Wind Speed'] = wind_desc(
                    five_day_forecast[day_key])
                formatted_forecast[day_key]['icon_id'] = icon_desc(five_day_forecast[day_key])

        for i, weather_report in enumerate(formatted_forecast.values()):
            ret_dict[i] = weather_report

        return ret_dict
