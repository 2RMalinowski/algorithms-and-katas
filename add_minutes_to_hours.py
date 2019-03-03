MIN_IN_HOUR = 60
HOURS_IN_DAY = 24


def add_minutes(hour, minute, minutes_to_add):
    '''
    Adds 'minutes_to_add' to a given time:

    >>> add_minutes(10, 30, 25)
    (10, 55)
    >>> add_minutes(10, 30, 50)
    (11, 20)
    >>> add_minutes(22, 30, 120)
    (0, 30)
    '''
    sum_of_minutes = minute + minutes_to_add
    hour += sum_of_minutes // MIN_IN_HOUR
    hour = hour % HOURS_IN_DAY
    sum_of_minutes %= MIN_IN_HOUR

    return hour, sum_of_minutes


# print(add_minutes(10, 30, 25))
# print(add_minutes(10, 30, 50))
# print(add_minutes(22, 30, 677))


# time format str HH:MM
def add_minutes(time, minutes_to_add):
    hour, minute = time.split(':')
    minutes_form_time = int(hour) * MIN_IN_HOUR + int(minute)
    sum_of_minutes = minutes_form_time + minutes_to_add
    hour = sum_of_minutes // MIN_IN_HOUR
    hour = hour % HOURS_IN_DAY
    minutes = sum_of_minutes % MIN_IN_HOUR

    return f'{hour:02}:{minutes:02}'  # 02 allow display extra 0 before one number hour or minute


print(add_minutes('23:55', 6))
