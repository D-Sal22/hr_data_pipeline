1) Which file appears to represent the most active period? Explain using at least two metrics. Consider that this is a 30 year old participant and compare your output to the column titled "Target HR Zone 50-85%" within this link: https://www.heart.org/en/healthy-living/fitness/fitness-basics/target-heart-rates

In my opinion, phase 2 appears to represent the most active period based on the range. It is the highest range and the list shows a greater spread in heart rate values. From my perspective the data with the most consistent spread would indicate increased activity in heart rate throught out the excercise period. It also has the most values that fall within the "Target HR Zone". Phase 2 also has the highest average and  median. 

2) Which file had the **poorest** data quality? How do you know?
Phase 4 has the poorest data, the length of this list is out of sync with the other data lists and can throw off the comparison. It also has a large amount of duplicates. The heart rate also does not fall within the target zone. Altough phase 0 has a large amount of values that also do not fall within the target zone, the amount of values in phase 0's dataset compliment in length in comparison to the other files. Perhaps Phase 0 could have been a "controlled" dataset to use in comparison to the others or the beginning of an exercise workout.   
...

3) Suppose one heart-rate file contains the following cleaned values: `68, 70, 71, 72, 72, 73, 74, 75, 180`. The value 180 was recorded during a sensor glitch.

a) Calculate the range of this dataset.
    range = 112


b) Explain how the extreme value affects the range.
    before_extreme_value = 7
    with_extreme_value = 112
    The extreme value skews the range and average. However, the median remains unchanged. The median in this dataset remains unchanged, but this may not always be true. The mid values just happen to be the same 72 and 72/2. It can really effect how the observer may intrepret the validity of the dataset and how spread out the data values may be.    


c) Identify a different statistic that would better represent the typical variability of the dataset. Why would this measure be better?
   A better statistic would have been the IQR, Interqaurtile Range, because it would measure the spread of the middle 50% of data and remains resistant to outliers. 
