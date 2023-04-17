from datetime import datetime
from datetime import timedelta


degree_sign = u'\N{DEGREE SIGN}'


def unix_to_dt(unix):
    return datetime.fromtimestamp(unix)


def time_from_dt(dt_object):
    return datetime.time(dt_object)


def increment_day_dt(dt_object, days):
    increment_value = timedelta(days=days)
    return dt_object + increment_value


def temp_desc(forecast):
    values = []
    for forecast_time in forecast:
        values.append(forecast_time['main']['temp'])
    return f"{kelvin_to_cels(min(values))}{degree_sign}C - {kelvin_to_cels(max(values))}{degree_sign}C"


def weather_desc(forecast):
    value = []
    for forecast_time in forecast:
        desc = forecast_time['weather'][0]['description']
        time_ = time_from_dt(unix_to_dt(forecast_time['dt']))
        time_string = time_.strftime("%H:%M")
        formatted_string = f"{time_string}: {desc}"
        value.append(formatted_string)
    return value


def kelvin_to_cels(K_temp):
    cels = K_temp - 273.15
    return round(cels, 1)


def m_s_to_mph(ms_speed):
    return round((ms_speed * 2.12585), 1)


def wind_desc(forecast):
    speed_values = []
    gust_values = []
    for forecast_time in forecast:
        speed_values.append(forecast_time['wind']['speed'])
        gust_values.append(forecast_time['wind']['gust'])

    return f"{m_s_to_mph(min(speed_values))} mph - {m_s_to_mph(max(speed_values))} mph"
