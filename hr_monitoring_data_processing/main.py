"""
The main Python module that combines cleaner and metrics functions in order to
perform comprehensive analysis
"""

from metrics import window_max, window_average, window_stddev
from cleaner import filter_nondigits, filter_outliers

import matplotlib.pyplot as plt


def run(filename: str) -> None:
    """
    Process heart rate data from the specified file, clean it, calculate metrics, 
    and save visualizations.

    Args:
        filename (str): The path to the data file (e.g., 'data/data1.txt').

    Steps:
        1. Read the file into a list of strings.
        2. Use `filter_nondigits` to clean the data and remove invalid entries.
        3. Use `filter_outliers` to remove unrealistic heart rate samples (<30 or >250).
        4. Calculate rolling maximums, averages, and standard deviations using functions from `metrics.py`.
        5. Save the plots to the `images/` folder:
            - Rolling maximums -> 'images/maximums.png'
            - Rolling averages -> 'images/averages.png'
            - Rolling standard deviations -> 'images/stdevs.png'

    Returns:
        list[int], list[int], list[int]: You will return the maximums, averages, and stdevs (in this order).
    """  
    data = []

    # open file and read into the `data` list
    file = open(filename)
    for f in file:
        data.append(f)
    file.close()
    
    data = filter_nondigits(data)
    
    data = filter_outliers(data)

    #window size of 6
    win_max = window_max(data, 6)

    #window size of 6
    win_avg = window_average(data, 6)

    #window size of 6
    std_dev = window_stddev(data, 6)

    #creates plot graph for maxes
    plt.plot(win_max)
    plt.savefig('images/maximums.png')
    plt.close()

    #creates plot graph for averages
    plt.plot(win_avg)
    plt.savefig('images/averages.png')
    plt.close()

    #creates plot graph for standard deviations
    plt.plot(std_dev)
    plt.savefig('images/stdevs.png')
    plt.close()

    # return all 3 lists
    return win_max, win_avg, std_dev


if __name__ == "__main__":
    run("data/data1.txt")