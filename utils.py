from datetime import datetime
from datetime import timedelta


def unix_to_dt(unix):
   return datetime.fromtimestamp(unix)

def time_from_dt(dt_object):
   return datetime.time(dt_object)

def increment_day_dt(dt_object, days):
   increment_value = timedelta(days=days)
   return dt_object + increment_value


