import statistics as stats


def average(data: list) -> float:
    """
    Calculate average of a list of integers using a for-loop. Assumes data is clean.
    """
    average = stats.mean(data)
    return average 

def median(data: list) -> float:

    median = stats.median(data)
    return median

def range(data: list) -> float:
   
    x = sorted(data)
    max_value = x[-1]
    min_value = x[0]

    data_range = max_value - min_value

    return data_range

