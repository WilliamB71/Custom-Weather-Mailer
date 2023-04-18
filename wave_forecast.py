import requests
import arrow
import statistics
from weather_forecast import Weather
from utils import m_s_to_mph


class StormGlass(Weather):

    def data():
        ret_dict = {}
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

        for day, data_list in ocean_data_raw.items():
            for param in parameters:
                day_values = []
                for timestamp in data_list:
                    if param == 'windSpeed':
                        try:
                            day_values.append(m_s_to_mph(
                                timestamp[param]['meto']))
                        except:
                            day_values.append(
                                m_s_to_mph(timestamp[param]['sg']))
                    else:
                        try:
                            day_values.append(timestamp[param]['meto'])
                        except:
                            day_values.append(timestamp[param]['sg'])

                ocean_data_clean[day][param] = f"{round(min(day_values), 1)} - {round(max(day_values), 1)}"

        for i, forecast_data in enumerate(ocean_data_clean.values()):
            ret_dict[i] = forecast_data

        return ret_dict
