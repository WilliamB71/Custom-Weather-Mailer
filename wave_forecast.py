import requests
import arrow
import statistics
from weather_forecast import Weather
from utils import m_s_to_mph


class StormGlass(Weather):

    def data():
        sunrise, sunset = StormGlass.daylight_times()
        timezone = 'Europe/London'
        start = arrow.now(tz=timezone).floor('day')
        end = arrow.now().shift(days=3).ceil('day')
        parameters = ['windSpeed', 'windWaveHeight', 'windWavePeriod',
                      'waterTemperature', 'swellPeriod', 'waveHeight', 'wavePeriod', 'swellHeight']

        response = requests.get(
            'https://api.stormglass.io/v2/weather/point',
            params={
                'lat': 50.6979,
                'lng': -1.91694,
                'params': ','.join(parameters),
                'start': start.to('UTC').timestamp(),
                'end': end.to('UTC').timestamp()},
            headers={
                'Authorization': '89cca680-b29a-11ed-a654-0242ac130002-89cca6f8-b29a-11ed-a654-0242ac130002'
            })

        json_data = response.json()

        ocean_data_raw = {arrow.now().format('DD-MM'): [],
                          arrow.now().shift(days=1).format('DD-MM'): [], arrow.now().shift(days=2).format('DD-MM'): []}

        for data_point in json_data.get('hours'):
            timestamp = arrow.get(data_point.get('time')).datetime

            if sunrise.time() <= timestamp.time() <= sunset.time():
                delta = (arrow.now() - timestamp).days

                try:
                    ocean_data_raw[list(ocean_data_raw.keys())[
                        delta]].append(data_point)
                except IndexError:
                    continue

        ocean_data_clean = {date: {} for date in ocean_data_raw}

        for day, data in ocean_data_raw.items():
            for param in parameters:
                values = []
                for timestamp in data:
                    values.append(statistics.median(
                        timestamp.get(param).values()))
                ocean_data_clean[day][param] = (min(values), max(values))
        return ocean_data_clean

    def report():
        wave_dict = StormGlass.data()
        humanise_parameter = {'windSpeed': 'Wind Speed (mph)', 'windWaveHeight': 'Wind Wave Height (ft)',
                              'waterTemperature': 'Water Temperature (°C)', 'waveHeight': 'Wave Height (ft)', 'wavePeriod': 'Wave Period (s)'}
        return_report = {day: {} for day in wave_dict}

        for day in wave_dict:
            for key in humanise_parameter:
                data = wave_dict[day][key]
                if data:
                    string_data = f"{round(data[0], 1)} - {round(data[1], 1)}"
                    if key == 'windSpeed':
                        string_data = f"{m_s_to_mph(data[0])} - {round(m_s_to_mph(data[1]), 1)}"
                    return_report[day][humanise_parameter[key]] = string_data
        return return_report

    def html_table():
        report = StormGlass.report()
        output_html = ''

        def html_formatter(weather_dict):
            table = "<table style='border-collapse: collapse; width: 80%; margin: auto; font-family: sans-serif;'>"
            table += "<tr style='background-color: #0099cc; color: white; text-align: center;'><th style='padding: 10px;'>Date</th><th style='padding: 10px;'>Wave Height (ft)</th><th style='padding: 10px;'>Wind Wave Height (ft)</th><th style='padding: 10px;'>Wave Period (s)</th><th style='padding: 10px;'>Wind Speed (mph)</th><th style='padding: 10px;'>Water Temperature (°C)</th></tr>"

            # Loop through each day's weather data
            for date, data in weather_dict.items():
                # Get the wind speed, wind wave height, water temperature, wave height, and wave period for the day
                wind_speed = data.get('Wind Speed (mph)', '')
                wind_wave_height = data.get('Wind Wave Height (ft)', '')
                water_temperature = data.get('Water Temperature (°C)', '')
                wave_height = data.get('Wave Height (ft)', '')
                wave_period = data.get('Wave Period (s)', '')

                # Add the data to the table row
                table += f"<tr style='text-align: center;'><td style='padding: 10px; background-color: #f2f2f2;'>{date.title()}</td><td style='padding: 10px;'>{wave_height}</td><td style='padding: 10px;'>{wind_wave_height}</td><td style='padding: 10px;'>{wave_period}</td><td style='padding: 10px;'>{wind_speed}</td><td style='padding: 10px;'>{water_temperature}</td></tr>"

            # Close the HTML table
            table += "</table>"

            # Return the HTML table
            return table

        for date, values in report.items():
            output_html += html_formatter({date: values})
            output_html += "<br>"

        return output_html
