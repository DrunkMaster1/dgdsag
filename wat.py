def seconds_difference(time_1, time_2):
    """ (number, number) -> number

    Return the number of seconds later that a time in seconds
    time_2 is than a time in seconds time_1.
        
    >>> seconds_difference(1800.0, 3600.0)
    1800.0
    >>> seconds_difference(3600.0, 1800.0)
    -1800.0
    >>> seconds_difference(1800.0, 2160.0)
    360.0
    >>> seconds_difference(1800.0, 1800.0)
    0.0
    """
    return time_2-time_1


def hours_difference(time_1, time_2):
    """ (number, number) -> float

    Return the number of hours later that a time in seconds
    time_2 is than a time in seconds time_1.
        
    >>> hours_difference(1800.0, 3600.0)
    0.5
    >>> hours_difference(3600.0, 1800.0)
    -0.5
    >>> hours_difference(1800.0, 2160.0)
    0.1
    >>> hours_difference(1800.0, 1800.0)
    0.0
    """
    hours = seconds_difference (time_1, time_2)/60
    return  hours /60


def to_float_hours(hours, minutes, seconds):
    """ (int, int, int) -> float

    Return the total number of hours in the specified number
    of hours, minutes, and seconds.

    Precondition: 0 <= minutes < 60  and  0 <= seconds < 60

    >>> to_float_hours(0, 15, 0)
    0.25
    >>> to_float_hours(2, 45, 9)
    2.7525
    >>> to_float_hours(1, 0, 36)
    1.01
    """
    hms = (hours * 60 * 60 + minutes *60 + seconds) /60
    return hms / 60


### Write your get_hours function definition here:


def get_hours(hours):
    """ (int) -> int

    Кeturns all hours in seconds

    >>> get_hours(3600)
    1"""
    
    hms = hours % 3600
    return (hours - hms) // 3600





### Write your get_minutes function definition here:
def get_minutes(minutes):
    """ (int) -> int

    Кeturns all minutes in seconds

    >>> get_minutes(3800)
    3"""
    hms = minutes  % 3600 
    hms1 = hms % 60
    return ( hms - hms1) // 60





### Write your get_seconds function definition here:

def get_seconds(seconds):
    """ (int) -> int

    Кeturns seconds

    >>> get_seconds(3800)
    20"""
    hms3 = seconds %3600 % 60
    return hms3

def time_to_utc(utc_offset, time):
    """ (number, float) -> float

    Return time at UTC+0, where utc_offset is the number of hours away from
    UTC+0.

    >>> time_to_utc(+0, 12.0)
    12.0
    >>> time_to_utc(+1, 12.0)
    11.0
    >>> time_to_utc(-1, 12.0)
    13.0
    >>> time_to_utc(-11, 18.0)
    5.0
    >>> time_to_utc(-1, 0.0)
    1.0
    >>> time_to_utc(-1, 23.0)
    0.0
    """
    time_utc = time - utc_offset
    if time_utc >= 24:
          return time_utc %24
    return time_utc      
 


def time_from_utc(utc_offset, time):
    """ (number, float) -> float

    Return UTC time in time zone utc_offset.

    >>> time_from_utc(+0, 12.0)
    12.0
    >>> time_from_utc(+1, 12.0)
    13.0
    >>> time_from_utc(-1, 12.0)
    11.0
    >>> time_from_utc(+6, 6.0)
    12.0
    >>> time_from_utc(-7, 6.0)
    23.0
    >>> time_from_utc(-1, 0.0)
    23.0
    >>> time_from_utc(-1, 23.0)
    22.0
    >>> time_from_utc(+1, 23.0)
    0.0
    """
    time_utc = time + utc_offset
    if time_utc < 0 :
          return 24 +time_utc 
    elif time_utc >=24 :     
         return time_utc - 24
    return time_utc          
print  (time_from_utc(+1, 12.0))  
