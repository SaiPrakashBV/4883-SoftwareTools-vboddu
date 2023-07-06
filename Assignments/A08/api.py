
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import csv



description = """🚀
## 4883 Software Tools -Assignment 08 - Fast API with Covid Data
### Where awesomeness happens
"""


app = FastAPI(

    description=description,

)

db = []

"The code reads the CSV file and populates the db list with the data from the CSV file, skipping the header row."
with open('D:\\4883-SoftwareTools-vboddu\\Assignments\\A08\\data.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    i = 0
    # Read each row in the CSV file
    for row in reader:
        if i == 0:
            i += 1
            continue
        db.append(row)

"The function getUniqueCountries() returns a list of unique countries from the db list."
def getUniqueCountries():
    global db
    countries = {}

    for row in db:
        #print(row)
        if not row[2] in countries:
            countries[row[2]] = 0

    return list(countries.keys())

"The function getUniqueWhos() returns a list of unique WHO regions from the db list."
def getUniqueWhos():
    global db
    whos = {}

    for row in db:
        #print(row)
        if not row[3] in whos:
            whos[row[3]] = 0
   
    return list(whos.keys())

"""A route is defined for the base URL ("/") to redirect to the "/docs" route."""
@app.get("/")
async def docs_redirect():
    """Api's base route that displays the information created above in the ApiInfo section."""
    return RedirectResponse(url="/docs")

"""A route is defined for the "/countries/" URL to return a JSON response containing the unique countries."""
@app.get("/countries/")
async def countries():

    return {"countries":getUniqueCountries()}

"""A route is defined for the "/whos/" URL to return a JSON response containing the unique WHO regions."""
@app.get("/whos/")
async def whos():

    return {"whos":getUniqueWhos()}

"""A route is defined for the "/casesByRegion/" URL to return a JSON response containing the number of cases by region.
 The response can be filtered by a specific year if provided."""
@app.get("/casesByRegion/")
async def casesByRegion(year:int = None):
    """
    Returns the number of cases by region

    """

    # create a dictionary as a container for our results
    # that will hold unique regions. Why, because there 
    # cannot be duplicate keys in a dictionary.
    cases = {}

    # return {'success':False,'message':'no database exists'}

    # loop through our db list
    for row in db:
        
        # If there is a year passed in and that year is not equal to this row
        # then skip the rest of code
        #print(int(row[0][-4:]))
        if year != None and year != int(row[0][-4:]):
            continue
            
        # this line guarantees that the dictionary has the region as a key
        if not row[3] in cases:
            cases[row[3]] = 0
        
        # this line adds the case count to whatever is at that key location
        cases[row[3]] += int(row[4])    

    # return cases

    return {"data":cases,"success":True,"message":"Cases by Region","size":len(cases),"year":year}

"""A route is defined for the "/deaths/" URL to return a JSON response containing death information based 
on the providedparameters (region, country, and year). The response can be filtered based on the combination of 
these parameters."""
@app.get("/deaths/")
async def get_deaths(region:str =None ,country:str =None, year:int =None):
    if region==None and country ==None and year == None:
        totalDeaths=0
        for row in db:
            totalDeaths += int(row[6])
        return {"Total Deaths":totalDeaths,"success":True}
    
    elif region!=None and country ==None and year == None:
        deaths={}
        deaths[region]=0
        for row in db:
             if  region == row[3]:
                deaths[row[3]] += int(row[6])

        return {"data":deaths,"success":True,"message":"Deaths of Region","Region":region,"size":len(deaths)}
    
    elif region!=None and country ==None and year != None:
        deaths={}
        deaths[region]=0
        for row in db:

            if region != None and region == row[3] and year != None and year == int(row[0][-4:]):
                deaths[row[3]] += int(row[6])
            
        return {"data":deaths,"success":True,"message":"Deaths of Region in a Year","Region":region,"Year":year}

    
    elif region==None and country !=None and year == None:
        deaths={}
        deaths[country]=0
        for row in db:
            if country==row[2]:
                deaths[row[2]]+=int(row[6])
        return {"data":deaths,"success":True,"message":"Deaths in a Country","Country":country,"size":len(deaths)}
    
    elif region==None and country !=None and year != None:
        deaths={}
        deaths[country]=0
        for row in db:

            if  country == row[2] and year == int(row[0][-4:]):
                deaths[row[2]] += int(row[6])

        return {"data":deaths,"success":True,"message":"Deaths of Country in a Year","Country":country,"Year":year}
    
    elif region==None and country ==None and year != None:
        deaths = {}
        for row in db:

            if year != int(row[0][-4:]):
                continue

            if not row[2] in deaths:
                deaths[row[2]] = 0

            deaths[row[2]] += int(row[6])    

        return {"data":deaths,"success":True,"message":"Deaths by Year in all countries","year":year,"size":len(deaths)}
    
    elif region!=None and country !=None and year == None:
        deaths={}
        deaths[country]=0
        for row in db:

            if  country == row[2] and region==row[3]:
                deaths[row[2]] += int(row[6])

        return {"data":deaths,"success":True,"message":"Deaths of Country in region","Country":country,"Region":region}

"""A route is defined for the "/cases/" URL to return a JSON response containing case information based on the 
provided parameters (region, country, and year). The response can be filtered based on the combination of these parameters."""
@app.get("/cases/")
async def get_cases(region:str =None ,country:str =None, year:int =None):
    if region==None and country ==None and year == None:
        totalCases=0
        for row in db:
            totalCases += int(row[4])
        return {"Total Cases":totalCases,"success":True}
    
    elif region!=None and country ==None and year == None:
        cases={}
        cases[region]=0
        for row in db:
             if  region == row[3]:
                cases[row[3]] += int(row[4])

        return {"data":cases,"success":True,"message":"cases of Region","Region":region,"size":len(cases)}
    
    elif region!=None and country ==None and year != None:
        cases={}
        cases[region]=0
        for row in db:

            if region != None and region == row[3] and year != None and year == int(row[0][-4:]):
                cases[row[3]] += int(row[4])
            
        return {"data":cases,"success":True,"message":"cases of Region in a Year","Region":region,"Year":year}

    
    elif region==None and country !=None and year == None:
        cases={}
        cases[country]=0
        for row in db:
            if country==row[2]:
                cases[row[2]]+=int(row[4])
        return {"data":cases,"success":True,"message":"cases in a Country","Country":country,"size":len(cases)}
    
    elif region==None and country !=None and year != None:
        cases={}
        cases[country]=0
        for row in db:

            if  country == row[2] and year == int(row[0][-4:]):
                cases[row[2]] += int(row[4])

        return {"data":cases,"success":True,"message":"cases of Country in a Year","Country":country,"Year":year}
    
    elif region==None and country ==None and year != None:
        cases = {}
        for row in db:

            if year != int(row[0][-4:]):
                continue

            if not row[2] in cases:
                cases[row[2]] = 0

            cases[row[2]] += int(row[4])    

        return {"data":cases,"success":True,"message":"cases by Year in all countries","year":year,"size":len(cases)}
    
    elif region!=None and country !=None and year == None:
        cases={}
        cases[country]=0
        for row in db:

            if  country == row[2] and region==row[3]:
                cases[row[2]] += int(row[4])

        return {"data":cases,"success":True,"message":"cases of Country in region","Country":country,"Region":region}

"""A route is defined for the "/max_deaths/" URL to return a JSON response containing the country with the maximum number of deaths.
 The response includes the maximum deaths, success status, message, and the size of the deaths dictionary."""
@app.get("/max_deaths/")
async def get_max_deaths():
    deaths = {}
    for row in db:
        if not row[2] in deaths:
            deaths[row[2]] = 0

        deaths[row[2]] += int(row[6])  

    max_deaths=max(deaths)  

    return {"data":max_deaths,"success":True,"message":"Maximum deaths by Country","size":len(deaths)}

"""A route is defined for the "/max_deaths_with_in_date_range/" URL to return a JSON response containing the maximum deaths
 within a specified date range. The response includes the deaths by country, success status, message, and the size of the 
 deaths_by_country dictionary."""
@app.get("/max_deaths_with_in_date_range/")
async def max_deaths_with_in_date_ranges(min_date:str =None, max_date:str =None):
    deaths_by_country={}
    if min_date !=None and max_date!=None:
        for row in db:
            if not row[2] in deaths_by_country:
                deaths_by_country[row[2]] = 0
            if min_date <=row[0]<=max_date:
                deaths_by_country[row[2]]+=int(row[6])
    
    return {"data":deaths_by_country,"success":True,"message":"Maximum deaths by Country","size":len(deaths_by_country)}



@app.get("/min_deaths/")
async def get_min_deaths():
    deaths = {}
    for row in db:
        if not row[2] in deaths:
            deaths[row[2]] = 0

        deaths[row[2]] += int(row[6])  

    min_deaths=min(deaths)  

    return {"data":min_deaths,"success":True,"message":"Minimum deaths by Country","size":len(deaths)}

@app.get("/avg_deaths/")
async def get_avg_deaths():
    deaths = {}
    total =0
    for row in db:
        if not row[2] in deaths:
            deaths[row[2]] = 0

        deaths[row[2]] += int(row[6])  
    for val in deaths.values():
        total+=val

    avg_deaths=int(total/len(deaths))

    return {"data":avg_deaths,"success":True,"message":"Average deaths by Country","size":len(deaths)}



if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=5000, log_level="debug", reload=True) #host="127.0.0.1"
