import pytz
import datetime

tz_Ame_New = pytz.timezone('America/New_York')
dt_Ame_New = "2022-07-11 12:43:18.881077-04:00"
print(dt_Ame_New)

date_format = datetime.datetime.strptime(dt_Ame_New,
                                         "%m/%d/%Y %H:%M:%S.ssssss-04:00")
unix_time = datetime.datetime.timestamp(date_format)
print(unix_time)