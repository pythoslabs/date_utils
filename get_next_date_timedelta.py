#input format =  YYYY-MM-DD

from datetime import timedelta

def get_next_day(dt2):
    dt2 = datetime.datetime.strptime(dt2, "%Y-%m-%d")
    dt1 = dt2 + timedelta(days=1)
    return dt1.strftime("%Y-%m-%d")


#Usage 
get_next_day('2021-09-03')  
