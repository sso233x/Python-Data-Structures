def weekday_name(day_of_week):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    
    # Check if the day_of_week is between 1 and 7
    if 1 <= day_of_week <= 7:
        return days[day_of_week - 1]  # Subtract 1 because list indices start at 0
    else:
        return None
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """

print(weekday_name(4))