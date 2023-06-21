""" 
Description:
    This is an example gui that allows you to enter the appropriate parameters to get the weather from wunderground.
TODO:
    - You will need to change the text input boxes to drop down boxes and add the appropriate values to the drop down boxes.
    - For example the month drop down box should have the values 1-12.
    - The day drop down box should have the values 1-31.
    - The year drop down box should have the values ??-2023.
    - The filter drop down box should have the values 'daily', 'weekly', 'monthly'.
"""
import PySimpleGUI as sg   
import json  
from get_weather_daily import * 

def currentDate(returnType='tuple'):
    """ Get the current date and return it as a tuple, list, or dictionary.
    Args:
        returnType (str): The type of object to return.  Valid values are 'tuple', 'list', or 'dict'.
    """
    from datetime import datetime
    if returnType == 'tuple':
        return (datetime.now().month, datetime.now().day, datetime.now().year)
    elif returnType == 'list':
        return [datetime.now().month, datetime.now().day, datetime.now().year]

    return {
        'day':datetime.now().day,
        'month':datetime.now().month,
        'year':datetime.now().year
    }

def buildWeatherURL(month=None, day=None, year=None, airport=None, filter=None):
    """ A gui to pass parameters to get the weather from the web.
    Args:
        month (int): The month to get the weather for.
        day (int): The day to get the weather for.
        year (int): The year to get the weather for.
    Returns:
        Should return a URL like this, but replace the month, day, and year, filter, and airport with the values passed in.
        https://www.wunderground.com/history/daily/KCHO/date/2020-12-31
    """
    current_month,current_day,current_year = currentDate('tuple')
    
    if not month:
        month = current_month
    if not day:
        day = current_day
    if not year:
        year = current_year
    Month=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    Day=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12","13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24","25", "26", "27", "28", "29", "30", "31"]
    Year=["2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021","2022","2023"
]
    data=[]
    with open('D:\\4883-SoftwareTools-vboddu\\Assignments\\A07\\airports-better.json') as f:
        data = json.load(f)
    
    airportcode=[]
    for e in data:
        airportcode.append(e["icao"])
    filter=["daily", "monthly", "weekly"]
    # Create the gui's layout using text boxes that allow for user input without checking for valid input
    layout = [
        [sg.Text('Month')],[sg.Combo(Month,readonly=True,)],
        [sg.Text('Day')],[sg.Combo(Day,readonly=True)],
        [sg.Text('Year')],[sg.Combo(Year,readonly=True)],
        [sg.Text('Code')],[sg.Combo(airportcode,readonly=True)],
        [sg.Text('Daily / Weekly / Monthly')],[sg.Combo(filter, readonly=True)],
        [sg.Submit(), sg.Cancel()]
    ]      

    window = sg.Window('Get The Weather', layout, finalize=True, element_justification='c')
    window.maximize()   

    event, values = window.read()
    window.close()
    Month_Number={"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}
    month = values[0]
    m=Month_Number[month]
    day = values[1]
    year = values[2]
    code = values[3]
    filter = values[4]


    
    url= f"https://www.wunderground.com/history/{filter}/{code}/date/{year}-{m}-{day}"
    sg.popup('You entered', f"Month: {month}, Day: {day}, Year: {year}, Code: {code}, Filter: {filter}",'URL is ',url, 'Getting the data from website...This may take  few moments....Please wait')
    return url
    # return the URL to pass to wunderground to get appropriate weather data

if __name__=='__main__':
    url= buildWeatherURL()
    #url="https://www.wunderground.com/history/daily/us/ok/lawton/KLAW/date/2023-6-13"
    page= asyncGetWeather(url)
    title, headers, column_data = get_data(page)
    #print(get_data(page))
    #empty=[]
    #sg.popup(f"{title}{headers}")
    #print(column_data)
    layout = [
    [sg.Table(values=column_data, headings=headers, max_col_width=25,
              auto_size_columns=True, display_row_numbers=True,
              justification='center', num_rows=10, key='-TABLE-')],
    [sg.Button('Exit')]
    ]

    # Create the window
    window = sg.Window('Daily Observations', layout)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break

    # Close the window
    window.close()
