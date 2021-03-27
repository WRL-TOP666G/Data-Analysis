import calendar
import datetime

def  number_of_days(year,month):
    '''
    Write a function that returns the number of calendar days in a given year and month. Hint: see the calendar module in the standard library. number_of_days(year,month)
    '''


    assert isinstance(year,int)
    assert isinstance(month,int)
    assert year>0
    assert month>0 and month<13
    return calendar.monthrange(year,month)[1]
    

def number_of_leap_years(year1,year2):
    '''
    Write a function to find the number of leap-years between (including both endpoints) two given years. number_of_leap_years(year1,year2)
    '''
    assert isinstance(year1,int)
    assert isinstance(year2,int)
    assert year1>0 and year2>0 and year2>=year1
    output=[]
    for year in range(year1, year2+1):
        if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
            output.append(year)
    return len(output)

def get_day_of_week(year,month,day):
    '''
    Write a function to find the string name (e.g., Monday, Tuesday) of the day of the week on a given month,day, and year. get_day_of_week(year,month,day)
    '''
    assert isinstance(year,int)
    assert isinstance(month,int)
    assert isinstance(day,int)
    assert datetime.datetime(year,month,day)
    dayNumber=calendar.weekday(year,month,day)
    days =["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return (days[dayNumber])


