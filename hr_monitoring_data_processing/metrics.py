def window_max(data: list, n: int) -> list:
    """
    Calculate maximum value of every "n"-size window

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: list of maximums from each window (size should be len(data)//6)
    """
    maximums = []
    #range start at 0, stops at the length of the list, steps by n
    for i in range (0, len(data), n):
        #slices list from index to index + window and assign to mx
        mx = data[i : i + n]
        #gets the max of the mx list and appends to maximums list
        maximums.append(max(mx))
    return maximums    
        

def window_average(data: list, n: int) -> list:
    """""
    Calculate the average of every n-size window

    Args:
        data(list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: list of averages from each window size
    """""
    averages = []
    #range start at 0, stops at the length of the list, steps by n
    for i in range (0, len(data), n):
        #slices list from index to index + window
        window = data[i : i + n]
        avg = sum(window) / len (window)
        #round the average to 2 decimal places and then append
        averages.append(round(avg, 2))
    return averages

def window_stddev(data: list, n: int) -> list:
    """""
    Calculate the standard deviation of every n-size window

    Args:
        data(list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: list of stdddevs from each window size
    """""
    stddevs = []
    #range start at 0, stops at the length of the list, steps by n
    for i in range (0, len(data), n):
        window = data[i : i + n]
        #skip over a window with only one number
        if len(window) == 1:
            continue
        mean = sum(window) / len (window)
        #find the variance
        variance = sum((i - mean) ** 2 for i in window) / (len(window) - 1)
        dev = variance ** 0.5
        #round the dev to 2 decimal places and then append
        stddevs.append(round(dev, 2))
    return stddevs