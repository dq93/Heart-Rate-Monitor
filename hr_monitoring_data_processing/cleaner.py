def filter_nondigits(data: list) -> list:
    """
    Filter all strings from list that are not integers

    Args:
        data (list[str]): list of strings representing heart rate samples.
            Might contain invalid or missing data.
    Returns:
        list[int]: list of integers, with all non-digit strings removed
    """
    #early return in case of an empty list
    if len(data) == 0:
        return data

    newData = []
    for d in data:
        #get rid of newline character
        d = d.strip('\n')
        #checks if string would be a digit
        if d.isdigit():
            #casts string as int and then appends
            newData.append(int(d))
    return newData

def filter_outliers(data: list) -> list:
    """
    Filters all integers that are not within the exclusive range of 30 and 250.

    Args:
        data (list[int]): list if integers that represent heart rate samples.
    Returns:
        list[int]: list of integers within 30 and 250 exclusive.
    """
    #early return in case of an empty list
    if len(data) == 0:
        return data
    
    newData = []
    for d in data:
        if 30 < d < 250:
            newData.append(d)
    return newData
