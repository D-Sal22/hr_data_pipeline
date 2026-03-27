def clean_heartrate_data(data: list) -> tuple:
    """
    Clean raw heart rate data by removing malformed or empty space data
    """
    new_list  = []
    
    for e in data:

       val = e.strip()
       if val != "" and val != "NO DATA": 
        
        new_val = int(val)
        new_list.append(new_val)
         

    return new_list 