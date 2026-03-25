def clean_heartrate_data(data: list) -> tuple: # is (data:list what we would call typecasting? )
    """
    Clean raw heart-rate data by removing malformed or impossible values.
    """
    cleaned = []

    for value in data:
        if isinstance(value, int): #is this supposed to be a colon? or a comma?
            cleaned.append(value)  #I used 'clean instead of cleaned.. copilot helped me find the "indentation error iw as reciveing"

    return cleaned


def average(data: list) -> float:
    """
    Calculate average of a list of integers using a for-loop. Assumes data is clean.
    """
    total = 0
    count = 0
    for value in data: 
        total = total + value
        count = count + 1
    
    return total/count

    


def median(data: list) -> float:
    """
    """
    hsort = sorted(data)
    n = len(hsort)
    hr_median = n//2
    # I asked goggle for examples of modulo that gave if statemets - if the number was even or odd, what the output would be
    # a recent update to my laptop is missing some of my notes in One Note
    if n % 2 == 1:
        return hsort[hr_median]
    else:
        return((hsort[hr_median -1] + hsort[hr_median])/2) ## 'mid_index -1 indicated the # to the right if there are two middle number so we are -1(one over to the right) middle number from the other in a sorted list. we add both values,then, dividing it by 2 to ge the median if the median presents two values by way of the counter.


def range(data: list) -> float:
    """
    """
    x = sorted(data)
    max_value = x[-1]
    min_value = x[0]

    data_range = max_value - min_value

    return data_range

def rolling_avg(data: list, k: int) -> float:
    """
    CHALLENGE FUNCTION (Optional)
    """
    pass


def run(file: str):
    """
    Process heart rate data from the a file by cleaning and
    calculating summary statistics. Print out final values.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, median, and range.
    """
    data = []

    # open file using file I/O and read it into the `data` list
    ...

    # Use `clean_heartrate_data` to clean the data and remove invalid entries
    cleaned_list, removed_values = ...

    # calculate the average, median, and range of this file using the functions you've wrote
    ...

    # print out your data quality measure to the console
    ...

    # print out your descriptive statistics to the console
    ...


if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")
