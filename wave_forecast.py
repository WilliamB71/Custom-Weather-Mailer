import requests 
import arrow
import statistics
from weather_forecast import Weather

class StormGlass(Weather):

    def report():
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


        ocean_data_raw = {'Today': [], 'Tomorrow': [], 'Day After Tomorrow': []}

        for data_point in json_data.get('hours'):
            timestamp = arrow.get(data_point.get('time')).datetime

            if sunrise.time() <= timestamp.time() <= sunset.time():
                delta = (arrow.now() - timestamp).days

                try:
                    ocean_data_raw[list(ocean_data_raw.keys())[delta]].append(data_point)
                except IndexError:
                    continue

        ocean_data_clean = {'Today': {}, 'Tomorrow': {}, 'Day After Tomorrow': {}}

        for day, data in ocean_data_raw.items():
            for param in parameters:
                values = []
                for timestamp in data:
                    values.append(statistics.median(timestamp.get(param).values()))
                ocean_data_clean[day][param] = (min(values), max(values))
        return ocean_data_clean

print(StormGlass.report())

# speed m/s
# wave heights m
# water temp = C
# swell period s

