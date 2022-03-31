# Returns in the format : YYYY_mm_dd_HH_MM_SS    ( year_month_date_hour_minute_second )
# eg: 2018_10_21_12_38_13
#  Useful to put a time stamp on a file that is created or in logging.
import datetime


def get_current_time_stamp():
    time_now = datetime.datetime.now()
    date_time_now = time_now.strftime('%Y' + "_" + '%m' + '_' + '%d' + '_' + '%H' + '_' + '%M' + '_' + '%S')
    return date_time_now
