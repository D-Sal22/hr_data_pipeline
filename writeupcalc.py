Phase0_list = [69, 75, 84, 79, 72, 69, 93, 91, 72, 76, 69, 71, 60, 63, 67, 58, 63, 61, 65, 66, 62, 61, 63, 61, 78, 62, 60, 59, 75, 65, 64, 60, 60, 63, 62, 68, 63, 61, 66, 56, 56, 54, 54, 54, 79, 68, 55, 55, 67, 58, 62, 60, 62, 70, 60, 55, 55, 57, 57, 56]
new_list = sorted(Phase0_list)
first_value = new_list[0]
last_value = new_list[-1]
print("smallest hr",first_value, "largest hr", last_value)
print(f"Phase 0 range = {last_value - first_value}") # to do an f string correctly, you need to do the quotes outside the curly braces 

average = sum(new_list)/len(new_list)
print("Phase0_avg =", average)
##""smallest hr 54 largest hr 93, Phase 0 range = 39 ,Phase0_avg = 64.76666666666667""