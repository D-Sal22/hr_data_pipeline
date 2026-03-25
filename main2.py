###"'with open("./data/phase0.txt", "r") as file_object:'""
#'Perform file operations inside this block'
#'for line in file_object:'
#'line = line.strip()'
#'if (line == 'NO DATA' or line == '' ):'
#'print(line)# the conditional should remove 'NO DATA" and none values'



def clean_heartrate_data(data: list) -> tuple:

    clean_heartrate_data = []
    
    for h in data:
        if(h == "NO DATA" or h == ""):  #I need to find the none''values and NO DATA strings.I used or conditional string. I dont need to put a comma or colon here
            data.remove(h)
        else:
            clean_heartrate_data.append(int(h)) #print only the values I need, append the value to an integer
    
    
    return clean_heartrate_data



def average(data: list) -> float:
    """
    Calculate average of a list of integers using a for-loop. Assumes data is clean.
    """
    total = 0
    count = 0
    for value in data: 
        total = total + value
        count = count + 1   #update with the newest bigger value> increase increments as opposed to -1, updates with the smallest new value, decreases the current value> countdowns> decrement a counter
    
    return total/count

    


def median(data: list) -> float:
    """
    """
    hsort = sorted(data)
    n = len(hsort)
    hr_median = n//2
   
    if n % 2 == 1:                   # I asked goggle for examples of modulo that gave if statemets - if the number was even or odd, what the output would be
        return hsort[hr_median]            # a recent update to my laptop is missing some of my notes in One Note
    else:
        return((hsort[hr_median -1] + hsort[hr_median])/2) ## 'mid_index -1' indicated the # to the right if there are two middle numbers so we are -1(one over to the right) middle number from the other in a sorted list. we add both values,then, dividing it by 2 to ge the median if the median presents two values by way of the counter.


def range(data: list) -> float:
    """
    """
    x = sorted(data)
    max_value = x[-1]
    min_value = x[0]

    data_range = max_value - min_value

    return data_range

def rolling_avg(data: list, k: int) -> float:     #BELOW , I incl my interpretation of the answer 
    """
    CHALLENGE FUNCTION (Optional) - I included my code below with a few gaps/ notes where I got lost 
    """
    #cont_avg = []
    #cont_sum = 0
    #while k > 0:
       # k= k -1 
        #cont_sum += data[k] #here, once we then introduce the new loop header below on the next line, will it make the rules above obsolete ? 
                            # or will it be computed when we return the value at the end?

 ##after that line we introduce the for statement below
   # for i in range(len(data)-k):
        # here is what i dont know what to do next with i 
        # I know the next step will be  updating what "cont_sum will be"
        #perhaps  cont_sum is equal to  us subtracting the data.. leaving the window to the new data entering, basically replacing the new value with the old one
        #unsure what that would look like in code
        # Then eventually, we would get to 
        #                                   cont_avg.append(cont_sum/k)
        #                                     return cont_avg.





def run(file: str):
    data = []

    with open(file, "r") as file:  # r here is referencing read where "w" is write for the file open function 
            for line in file:
                data.append(line.replace("\n", "")) #I simplified, 'if (line == 'NO DATA' or line == '' ):'
              
    c_hr_list = clean_heartrate_data(data)           #my indents were causing me to receive errors - in defining c_hr_list   
    
    #-------Median-------          
    s = sorted(c_hr_list)
    n = len(c_hr_list)
    mid = n // 2
 
    if n % 2 == 1:
        median_value = c_hr_list[mid]
    else:
        median_value = (c_hr_list[mid - 1] + c_hr_list[mid]) / 2
    #---------Range ----------
    def hr_range(values: list) -> float:
    
            s = sorted(values)
            n = len(s)

            if len(s) > 0:
                return s[-1] - s[0]
            
    #------ Mean -------    
    average = sum(c_hr_list)/len(c_hr_list)
   
    print(sorted(c_hr_list))   # I realized it helped me better in the write up if the list was sorted to do comparison. I had to go back to median and range to add it. 
    print("length of list =", len(c_hr_list))       
    print(f"mean = {average:.2f}")  #I asked copilot methods to round two decimal places
    print("median = ", median_value)
    print("range = ", hr_range(c_hr_list))
    
    
# """
#     # # Process heart rate data from the a file by cleaning and
#     # # calculating summary statistics. Print out final values.

#     # # Args:
#     # #     filename (str): The path to the data file (e.g., 'data/phase0.txt').

#     # # Returns:
#     # #     float, float, float: You will return the average, median, and range.
    # # """
   

    #open file using file I/O and read it into the `data` list
    # # ...DONE

    # # # ""Use `clean_heartrate_data` to clean the data and remove invalid entries
    ###lsted here 👉🏿 cleaned_list, removed_values = [69, 51, 56, 53, 56, 54, 57, 57, 64, 60, 58, 57, 56, 56, 55, 54, 55, 53, 52, 55, 97, 67, 58, 57, 54, 56, 53, 52, 59, 76, 66, 62, 62, 62, 52, 53, 50, 51, 50, 52, 52, 51, 80, 73, 95, 88, 67, 62, 64, 61, 57, 60, 56, 55, 54, 53, 53, 54, 52, 53, 52, 51, 51, 56, 54, 59, 56, 79, 74, 70, 65, 58, 57, 54, 54, 54, 54, 65, 99, 91, 66, 85, 63, 64, 61, 67]""

    # # calculate the average, median, and range of this file using the functions you've wrote, DONE, above ⬆️
    # ...

    # # print out your data quality measure to the console 


    # # print out your descriptive statistics to the console ✅ complete
    # ...


if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")

