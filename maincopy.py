import hr_module as mod1
import statistics as stats
import cleaner

def rolling_avg(data: list, k: int) -> float:
    """
    CHALLENGE FUNCTION (Optional)
    """
    pass


def run(file: str):
    data = []

    with open(file, "r") as file:  
            for line in file:
                data.append(line.replace("\n", "")) 
              
    c_hr_list = cleaner.clean_heartrate_data(data)
  
    list_average = mod1.average(c_hr_list)
    list_median = mod1.median(c_hr_list)
    list_range = mod1.range(c_hr_list)

    print(list_average)
    print(list_median)
    print(list_range)

    # calculate the average, median, and range of this file using the functions you've wrote

    # print out your data quality measure to the console
 

    # print out your descriptive statistics to the console



if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")