def get_next_date(date_) : 

    '''
    Returns the next date ( check for leap year - not done )
       input format 2018-08-22 (YYYY-MM-DD) 
    Note : you can also use the built-in datetime module 
    This is a round about way.
    '''
    
    next_month = next_day =next_year = ''
    # create a dictionary of the max number of days in a month
    dict_month_days = {'01':31 , '02':28 ,'03' : 31,'04' : 30,'05' : 31,'06' : 30,'07' : 31,'08' : 31\
                      ,'09' : 30,'10' : 31,'11' : 30,'12' : 31}
    year, month, day  = split_date(date_)
    
    #Max value of days 
    max_days = dict_month_days.get(month)
    
    
    # If last day of the month ------------------- 
    if int(day) == max_days :
        next_month = int(month) + 1  if int(month) != 12 else int(month) 
        next_day = 1
    else : 
        next_month = int(month)
        next_day  = int(day) + 1 
    
    # If last day of the year -------------------
    if int(month) == 12 & int(day) == max_days: 
        next_day = 1 
        next_month = 1
        next_year = int(year) + 1
    
    #formatting , type conversion & zero-padding 
    if next_day < 10  : 
        next_day = '0'+str(next_day)
    else : next_day = str(next_day)
    
    if next_month < 10  : 
        next_month = '0'+str(next_month)
    else : next_month = str(next_month)
    
    next_year = str(year)
    
    return  (f"{next_year}-{next_month}-{next_day}")
    
    
#Usage 
get_next_date('2020-07-22')   
