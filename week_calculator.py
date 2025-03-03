import datetime
from datetime import timedelta

def remaining_business_days():
    today = datetime.datetime.now()
    weekday_index = datetime.date(today.year, today.month, today.day).weekday()
    start = datetime.date.today()
    # print(start)
    # print(weekday_index)
    future = datetime.date.today() + timedelta(days=4 - weekday_index)
    # print(future)
    return start, future