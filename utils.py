import arrow
from statistics import mode


degree_sign = u'\N{DEGREE SIGN}'


def unix_to_dt(unix):
    timestamp = arrow.get(unix)
    return timestamp.to('Europe/London')


def time_from_dt(dt_object):
    return arrow.Arrow.time(dt_object)


def increment_day_dt(dt_object, days):
    return dt_object.shift(days=days)


def temp_desc(forecast):
    values = []
    for forecast_time in forecast:
        values.append(forecast_time['main']['temp'])
    return f"{kelvin_to_cels(min(values))} - {kelvin_to_cels(max(values))}{degree_sign}C"


def icon_desc(forecast):
    values = []
    for forecast_time in forecast:
        values.append(forecast_time['weather'][0]['icon'])
    return mode(values)


def weather_desc(forecast):
    value = {}
    ret_list = []
    ret_str = ''
    for forecast_time in forecast:
        desc = forecast_time['weather'][0]['description']
        time_ = time_from_dt(unix_to_dt(forecast_time['dt']))
        time_string = time_.strftime("%H:%M")
        value[time_string] = desc

    for i, (t, description) in enumerate(value.items()):
        if not ret_list:
            ret_list.append((t, description))
            continue
        if description in ret_list[-1] and i < (len(list(value.keys()))-1):
            continue
        else:
            ret_list.append((t, description))

    for time, descr in ret_list:
        ret_str += f'<p>{time}: {descr}</p>'

    return ret_str


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

    return f"{m_s_to_mph(min(speed_values))} - {m_s_to_mph(max(speed_values))} mph"
