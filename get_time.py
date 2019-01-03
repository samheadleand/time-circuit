from datetime import datetime

def add_zero_to_datetimes(digits):
    if len(digits) == 1:
        return '0' + str(digits)
    else:
        return digits

def find_month_date(new_datetime):
    return add_zero_to_datetimes(str(new_datetime.month)) + add_zero_to_datetimes(str(new_datetime.day))

print(find_month_date(datetime.now()))

def find_year(new_datetime):
    return add_zero_to_datetimes(str(new_datetime.year))

def find_time(new_datetime):
    hour = new_datetime.hour
    minute = new_datetime.minute
    if hour >= 13:
        hour -= 12
        am_pm = 'pm'
    else:
        am_pm = 'am'
    hour = add_zero_to_datetimes(str(hour))
    minute = add_zero_to_datetimes(str(minute))
    return (am_pm, hour+minute)

