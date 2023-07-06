
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import csv
from datetime import datetime



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


@app.get("/deaths/")
async def get_deaths(region:str =None ,country:str =None, year:int =None):
    """A route is defined for the "/deaths/" URL to return a JSON response containing death information based 
        on the providedparameters (region, country, and year). The response can be filtered based on the combination of 
        these parameters."""
    """
    #### Example 1: [http://localhost:5000/deaths/](http://localhost:5000/deaths/)

    #### Response 1:{"Total Deaths":6945714,
                     "success":true,
                     "Region":null,
                     "country":null,
                     "Year":null}

    #### Example 2: [http://localhost:5000/deaths/?country=Afghanistan](http://localhost:5000/deaths/?country=Afghanistan)

    #### Response 2: {"data":{"Afghanistan":7922},
                      "success":true,
                      "message":"Deaths in a Country",
                      "Region":null,
                      "country":"Afghanistan",
                      "Year":null}
    
    #### Example 3:[http://localhost:5000/deaths/?region=EMRO](http://localhost:5000/deaths/?region=EMRO)

    #### Response 3:{"data":{"EMRO":351329},
                     "success":true,
                     "message":"Deaths of Region",
                     "Region":"EMRO",
                     "country":null,
                     "year":null}
    #### Example 4:[http://localhost:5000/deaths/?region=EMRO&year=2021](http://localhost:5000/deaths/?region=EMRO&year=2021)

    #### Response 4: {"data":{"EMRO":195342},
                      "success":true,
                      "message":"Deaths of Region in a Year",
                      "Region":"EMRO",
                      "country":null,
                      "Year":2021}  

    #### Example 5: [http://localhost:5000/deaths/?country=Afghanistan&year=2021](http://localhost:5000/deaths/?country=Afghanistan&year=2021)

    #### Response 5: {"data":{"Afghanistan":5167},
                      "success":true,
                      "message":"Deaths of Country in a Year",
                      "Region":null,
                      "country":"Afghanistan",
                      "Year":2021}

    #### Example 6: [http://localhost:5000/deaths/?year=2021](http://localhost:5000/deaths/?year=2021)

    #### Response 6:{"data":{"Afghanistan":5167,"Albania":2042,"Algeria":3520,"American Samoa":0,"Andorra":56,"Angola":1352,"Anguilla":5,"Antigua and Barbuda":114,"Argentina":69905,"Armenia":5149,"Aruba":132,"Australia":1523,"Austria":9318,"Azerbaijan":5771,"Bahamas":547,"Bahrain":1042,"Bangladesh":20513,"Barbados":253,"Belarus":4147,"Belgium":8682,"Belize":356,"Benin":117,"Bermuda":96,"Bhutan":3,"Bolivia (Plurinational State of)":10515,"Bonaire":19,"Bosnia and Herzegovina":9378,"Botswana":2409,"Brazil":426136,"British Virgin Islands":38,"Brunei Darussalam":58,"Bulgaria":23375,"Burkina Faso":233,"Burundi":12,"Cabo Verde":240,"Cambodia":3012,"Cameroon":1405,"Canada":14684,"Cayman Islands":9,"Central African Republic":38,"Chad":76,"Chile":22597,"China":911,"Colombia":87246,"Comoros":148,"Congo":269,"Cook Islands":0,"Costa Rica":5198,"CÃ´te dâ€™Ivoire":574,"Croatia":8633,"Cuba":8177,"CuraÃ§ao":173,"Cyprus":524,"Czechia":24444,"Democratic People's Republic of Korea":0,"Democratic Republic of the Congo":634,"Denmark":2000,"Djibouti":128,"Dominica":47,"Dominican Republic":1837,"Ecuador":19646,"Egypt":14151,"El Salvador":2496,"Equatorial Guinea":89,"Eritrea":74,"Estonia":1703,"Eswatini":1114,"Ethiopia":5008,"Falkland Islands (Malvinas)":0,"Faroe Islands":14,"Fiji":696,"Finland":1118,"France":56958,"French Guiana":268,"French Polynesia":522,"Gabon":224,"Gambia":219,"Georgia":11295,"Germany":68033,"Ghana":971,"Gibraltar":94,"Greece":15920,"Greenland":1,"Grenada":200,"Guadeloupe":676,"Guam":149,"Guatemala":11299,"Guernsey":8,"Guinea":310,"Guinea-Bissau":104,"Guyana":887,"Haiti":537,"Holy See":0,"Honduras":7323,"Hungary":29649,"Iceland":6,"India":332342,"Indonesia":121956,"Iran (Islamic Republic of)":76477,"Iraq":11346,"Ireland":3827,"Isle of Man":32,"Israel":4923,"Italy":63643,"Jamaica":2168,"Japan":14979,"Jersey":47,"Jordan":8805,"Kazakhstan":15478,"Kenya":3709,"Kiribati":0,"Kosovo[1]":1658,"Kuwait":1535,"Kyrgyzstan":1447,"Lao People's Democratic Republic":372,"Latvia":3935,"Lebanon":7659,"Lesotho":607,"Liberia":198,"Libya":4237,"Liechtenstein":25,"Lithuania":5597,"Luxembourg":413,"Madagascar":766,"Malawi":2166,"Malaysia":31024,"Maldives":214,"Mali":389,"Malta":258,"Marshall Islands":0,"Martinique":741,"Mauritania":523,"Mauritius":776,"Mayotte":130,"Mexico":156199,"Micronesia (Federated States of)":0,"Monaco":35,"Mongolia":1985,"Montenegro":1724,"Montserrat":0,"Morocco":7489,"Mozambique":1831,"Myanmar":16586,"Namibia":3437,"Nauru":0,"Nepal":8836,"Netherlands":9589,"New Caledonia":281,"New Zealand":26,"Nicaragua":52,"Niger":173,"Nigeria":1752,"Niue":0,"North Macedonia":5461,"Northern Mariana Islands (Commonwealth of the)":11,"Norway":958,"occupied Palestinian territory, including east Jerusalem":3431,"Oman":2986,"Other":0,"Pakistan":18874,"Palau":0,"Panama":3492,"Papua New Guinea":581,"Paraguay":14404,"Peru":109518,"Philippines":42274,"Pitcairn Islands":0,"Poland":68416,"Portugal":12095,"Puerto Rico":1643,"Qatar":372,"Republic of Korea":4725,"Republic of Moldova":7159,"RÃ©union":367,"Romania":43118,"Russian Federation":251841,"Rwanda":1263,"Saba":0,"Saint BarthÃ©lemy":4,"Saint Helena, Ascension and Tristan da Cunha":0,"Saint Kitts and Nevis":28,"Saint Lucia":290,"Saint Martin":27,"Saint Pierre and Miquelon":0,"Saint Vincent and the Grenadines":83,"Samoa":0,"San Marino":40,"Sao Tome and Principe":40,"Saudi Arabia":2661,"Senegal":1488,"Serbia":9525,"Seychelles":125,"Sierra Leone":47,"Singapore":799,"Sint Eustatius":0,"Sint Maarten":48,"Slovakia":14497,"Slovenia":3139,"Solomon Islands":0,"Somalia":1203,"South Africa":63028,"South Sudan":72,"Spain":37229,"Sri Lanka":14775,"Sudan":1776,"Suriname":1069,"Sweden":5639,"Switzerland":4393,"Syrian Arab Republic":2189,"Tajikistan":35,"Thailand":21637,"The United Kingdom":83496,"Timor-Leste":122,"Togo":180,"Tokelau":0,"Tonga":0,"Trinidad and Tobago":2699,"Tunisia":20944,"TÃ¼rkiye":61462,"Turkmenistan":0,"Turks and Caicos Islands":20,"Tuvalu":0,"Uganda":2993,"Ukraine":77366,"United Arab Emirates":1497,"United Republic of Tanzania":716,"United States of America":467051,"United States Virgin Islands":66,"Uruguay":6000,"Uzbekistan":871,"Vanuatu":0,"Venezuela (Bolivarian Republic of)":4300,"Viet Nam":32359,"Wallis and Futuna":7,"Yemen":1373,"Zambia":3344,"Zimbabwe":4637},"success":true,"message":"Deaths by Year in all countries","Region":null,"country":null,"Year":2021}
    
    #### Example 7: [http://localhost:5000/deaths/?region=EMRO&country=Afghanistan](http://localhost:5000/deaths/?region=EMRO&country=Afghanistan)

    #### Response 7: {"data":{"Afghanistan":7922},
                      "success":true,
                      "message":"Deaths of Country in region",
                      "Region":"EMRO",
                      "country":"Afghanistan",
                      "Year":null}
    """
    if region==None and country ==None and year == None:
        totalDeaths=0
        for row in db:
            totalDeaths += int(row[6])
        return {"Total Deaths":totalDeaths,"success":True,"Region":region,"country":country,"Year":year}
    
    elif region!=None and country ==None and year == None:
        deaths={}
        deaths[region]=0
        for row in db:
             if  region == row[3]:
                deaths[row[3]] += int(row[6])

        return {"data":deaths,"success":True,"message":"Deaths of Region","Region":region,"country":country,"year":year}
    
    elif region!=None and country ==None and year != None:
        deaths={}
        deaths[region]=0
        for row in db:

            if region != None and region == row[3] and year != None and year == int(row[0][-4:]):
                deaths[row[3]] += int(row[6])
            
        return {"data":deaths,"success":True,"message":"Deaths of Region in a Year","Region":region,"country":country,"Year":year}

    
    elif region==None and country !=None and year == None:
        deaths={}
        deaths[country]=0
        for row in db:
            if country==row[2]:
                deaths[row[2]]+=int(row[6])
        return {"data":deaths,"success":True,"message":"Deaths in a Country","Region":region,"country":country,"Year":year}
    
    elif region==None and country !=None and year != None:
        deaths={}
        deaths[country]=0
        for row in db:

            if  country == row[2] and year == int(row[0][-4:]):
                deaths[row[2]] += int(row[6])

        return {"data":deaths,"success":True,"message":"Deaths of Country in a Year","Region":region,"country":country,"Year":year}
    
    elif region==None and country ==None and year != None:
        deaths = {}
        for row in db:

            if year != int(row[0][-4:]):
                continue

            if not row[2] in deaths:
                deaths[row[2]] = 0

            deaths[row[2]] += int(row[6])    

        return {"data":deaths,"success":True,"message":"Deaths by Year in all countries","Region":region,"country":country,"Year":year}
    
    elif region!=None and country !=None and year == None:
        deaths={}
        deaths[country]=0
        for row in db:

            if  country == row[2] and region==row[3]:
                deaths[row[2]] += int(row[6])

        return {"data":deaths,"success":True,"message":"Deaths of Country in region","Region":region,"country":country,"Year":year}

"""A route is defined for the "/cases/" URL to return a JSON response containing case information based on the 
provided parameters (region, country, and year). The response can be filtered based on the combination of these parameters."""
@app.get("/cases/")
async def get_cases(region:str =None ,country:str =None, year:int =None):
    if region==None and country ==None and year == None:
        totalCases=0
        for row in db:
            totalCases += int(row[4])
        return {"Total Cases":totalCases,"success":True,"Region":region,"country":country,"Year":year}
    
    elif region!=None and country ==None and year == None:
        cases={}
        cases[region]=0
        for row in db:
             if  region == row[3]:
                cases[row[3]] += int(row[4])

        return {"data":cases,"success":True,"message":"cases of Region","Region":region,"country":country,"Year":year}
    
    elif region!=None and country ==None and year != None:
        cases={}
        cases[region]=0
        for row in db:

            if region != None and region == row[3] and year != None and year == int(row[0][-4:]):
                cases[row[3]] += int(row[4])
            
        return {"data":cases,"success":True,"message":"cases of Region in a Year","Region":region,"country":country,"Year":year}

    
    elif region==None and country !=None and year == None:
        cases={}
        cases[country]=0
        for row in db:
            if country==row[2]:
                cases[row[2]]+=int(row[4])
        return {"data":cases,"success":True,"message":"cases in a Country","Region":region,"country":country,"Year":year}
    
    elif region==None and country !=None and year != None:
        cases={}
        cases[country]=0
        for row in db:

            if  country == row[2] and year == int(row[0][-4:]):
                cases[row[2]] += int(row[4])

        return {"data":cases,"success":True,"message":"cases of Country in a Year","Region":region,"country":country,"Year":year}
    
    elif region==None and country ==None and year != None:
        cases = {}
        for row in db:

            if year != int(row[0][-4:]):
                continue

            if not row[2] in cases:
                cases[row[2]] = 0

            cases[row[2]] += int(row[4])    

        return {"data":cases,"success":True,"message":"cases by Year in all countries","Region":region,"country":country,"Year":year}
    
    elif region!=None and country !=None and year == None:
        cases={}
        cases[country]=0
        for row in db:

            if  country == row[2] and region==row[3]:
                cases[row[2]] += int(row[4])

        return {"data":cases,"success":True,"message":"cases of Country in region","Region":region,"country":country,"Year":year}

"""A route is defined for the "/max_deaths/" URL to return a JSON response containing the country with the maximum number of deaths.
 The response includes the maximum deaths, success status, message, and the size of the deaths dictionary."""
@app.get("/max_deaths/")
async def get_max_deaths():
    """
    #### Example 8: http://localhost:5000/max_deaths/

    #### Response 8:
                    {"data":"occupied Palestinian territory, including east Jerusalem",
                    "success":true,
                    "message":"Maximum deaths by Country",
                    "size":237}
    
    """
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
        minDate = datetime.strptime(min_date, '%y-%m-%d').date()
        maxDate = datetime.strptime(max_date, '%y-%m-%d').date()
        
        for row in db:
            curr_Date = datetime.strptime(row[0], '%m/%d/%y').date()
            if not row[2] in deaths_by_country:
                deaths_by_country[row[2]] = 0
            if min_date <=curr_Date<=max_date:
                deaths_by_country[row[2]]+=int(row[6])

    
    return {"data":deaths_by_country,"success":True,"message":"Maximum deaths by Country","size":len(deaths_by_country)}



@app.get("/min_deaths/")
async def get_min_deaths():
    """
    #### Example 9:[http://localhost:5000/min_deaths/](http://localhost:5000/min_deaths/)

    #### Response 9:
                    {"data":"Afghanistan",
                    "success":true,
                    "message":"Minimum deaths by Country",
                    "size":237}

    """

    deaths = {}
    for row in db:
        if not row[2] in deaths:
            deaths[row[2]] = 0

        deaths[row[2]] += int(row[6])  

    min_deaths=min(deaths)  

    return {"data":min_deaths,"success":True,"message":"Minimum deaths by Country","size":len(deaths)}

@app.get("/avg_deaths/")
async def get_avg_deaths():
    """
    Example 10: [http://localhost:5000/avg_deaths/](http://localhost:5000/avg_deaths/)

    Response 10: 
                {"data":29306,
                "success":true,
                "message":"Average deaths by Country",
                "size":237}
    
    """
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
