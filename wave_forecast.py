import requests 
import arrow
import statistics
from weather_forecast import Weather
from utils import m_s_to_mph

class StormGlass(Weather):

    def data():
        sunrise, sunset = StormGlass.daylight_times()
        timezone ='Europe/London'
        start = arrow.now(tz=timezone).floor('day')
        end =  arrow.now().shift(days=3).ceil('day')
        parameters = ['windSpeed', 'windWaveHeight', 'windWavePeriod', 'waterTemperature', 'swellPeriod', 'waveHeight', 'wavePeriod', 'swellHeight']



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

        print(json_data.get('meta'))


        ocean_data_raw = {arrow.now().format('DD-MM'): [],
                              arrow.now().shift(days=1).format('DD-MM'): [], arrow.now().shift(days=2).format('DD-MM'): []}

        for data_point in json_data.get('hours'):
            timestamp = arrow.get(data_point.get('time')).datetime

            if sunrise.time() <= timestamp.time() <= sunset.time():
                delta = (arrow.now() - timestamp).days

                try:
                    ocean_data_raw[list(ocean_data_raw.keys())[delta]].append(data_point)
                except IndexError:
                    continue

        ocean_data_clean = {date: {} for date in ocean_data_raw}

        for day, data in ocean_data_raw.items():
            for param in parameters:
                values = []
                for timestamp in data:
                    values.append(statistics.median(timestamp.get(param).values()))
                ocean_data_clean[day][param] = (min(values), max(values))
        return ocean_data_clean
    
    def report():
        wave_dict = StormGlass.data()
        humanise_parameter = {'windSpeed': 'Wind Speed (mph)', 'windWaveHeight': 'Wind Wave Height (m)', 'waterTemperature': 'Water Temperature (°C)', 'waveHeight': 'Wave Height (m)', 'wavePeriod': 'Wave Period (s)'}
        return_report = {day : {} for day in wave_dict}

        for day in wave_dict:
          for key in humanise_parameter:
            data = wave_dict[day][key]
            if data:
              string_data = f"{round(data[0], 1)} - {round(data[1], 1)}"
              if key == 'windSpeed':
                  string_data = f"{m_s_to_mph(data[0])} - {round(m_s_to_mph(data[1]), 1)}"
              return_report[day][humanise_parameter[key]] = string_data
        return return_report

print(StormGlass.report())



# speed m/s
# wave heights m
# water temp = C
# swell period s

