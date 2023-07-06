## Assignment 8 - Fast Api with Covid Data

### Venkata Sai Prakash Boddu

### Overview:

This code implements a FastAPI-based web application for retrieving and analyzing COVID-19 data. It provides various routes to access information such as cases, deaths, unique countries, and WHO regions.

The application starts by creating a FastAPI instance with a predefined description. It also initializes an empty list called `db` to store the COVID-19 data that will be read from a CSV file.

The code then reads the CSV file and populates the `db` list with the data, skipping the header row. This data serves as the source for all the subsequent data retrieval operations.

The application defines several routes:
1. The base URL ("/") redirects to the "/docs" route, which displays documentation for the API.
2. The "/countries/" route returns a JSON response containing the unique countries present in the data.
3. The "/whos/" route returns a JSON response containing the unique WHO regions present in the data.
4. The "/casesByRegion/" route returns the number of cases by region. It accepts an optional parameter for filtering by a specific year.
5. The "/deaths/" route provides flexibility for retrieving death information. It accepts parameters such as region, country, and year, allowing for customized data retrieval. It allows all combinations such as region alone, country alone, region & year, country & year, year alone and region & country.
    #### Example 1: [http://localhost:5000/deaths/](http://localhost:5000/deaths/)

    #### Response 1:
                    {"Total Deaths":6945714,
                     "success":true,
                     "Region":null,
                     "country":null,
                     "Year":null}

    #### Example 2: [http://localhost:5000/deaths/?country=Afghanistan](http://localhost:5000/deaths/?country=Afghanistan)

    #### Response 2: 
                    {"data":{"Afghanistan":7922},
                      "success":true,
                      "message":"Deaths in a Country",
                      "Region":null,
                      "country":"Afghanistan",
                      "Year":null}
    
    #### Example 3:[http://localhost:5000/deaths/?region=EMRO](http://localhost:5000/deaths/?region=EMRO)

    #### Response 3:
                    {"data":{"EMRO":351329},
                     "success":true,
                     "message":"Deaths of Region",
                     "Region":"EMRO",
                     "country":null,
                     "year":null}
    #### Example 4:[http://localhost:5000/deaths/?region=EMRO&year=2021](http://localhost:5000/deaths/?region=EMRO&year=2021)

    #### Response 4: 
                    {"data":{"EMRO":195342},
                      "success":true,
                      "message":"Deaths of Region in a Year",
                      "Region":"EMRO",
                      "country":null,
                      "Year":2021}  

    #### Example 5: [http://localhost:5000/deaths/?country=Afghanistan&year=2021](http://localhost:5000/deaths/?country=Afghanistan&year=2021)

    #### Response 5: 
                    {"data":{"Afghanistan":5167},
                      "success":true,
                      "message":"Deaths of Country in a Year",
                      "Region":null,
                      "country":"Afghanistan",
                      "Year":2021}

    #### Example 6: [http://localhost:5000/deaths/?year=2021](http://localhost:5000/deaths/?year=2021)

    #### Response 6:
                    {"data":{"Afghanistan":5167,
                    "Albania":2042,
                    "Algeria":3520,
                    "American Samoa":0,
                    "Andorra":56,
                    "Angola":1352,
                    "Anguilla":5,
                    "Antigua and Barbuda":114,
                    "Argentina":69905,
                    "Armenia":5149,"Aruba":132,"Australia":1523,"Austria":9318,"Azerbaijan":5771,"Bahamas":547,"Bahrain":1042,"Bangladesh":20513,"Barbados":253,"Belarus":4147,"Belgium":8682,"Belize":356,"Benin":117,"Bermuda":96,"Bhutan":3,"Bolivia (Plurinational State of)":10515,"Bonaire":19,"Bosnia and Herzegovina":9378,"Botswana":2409,"Brazil":426136,"British Virgin Islands":38,"Brunei Darussalam":58,"Bulgaria":23375,"Burkina Faso":233,"Burundi":12,"Cabo Verde":240,"Cambodia":3012,"Cameroon":1405,"Canada":14684,"Cayman Islands":9,"Central African Republic":38,"Chad":76,"Chile":22597,"China":911,"Colombia":87246,"Comoros":148,"Congo":269,"Cook Islands":0,"Costa Rica":5198,"CÃ´te dâ€™Ivoire":574,"Croatia":8633,"Cuba":8177,"CuraÃ§ao":173,"Cyprus":524,"Czechia":24444,"Democratic People's Republic of Korea":0,"Democratic Republic of the Congo":634,"Denmark":2000,"Djibouti":128,"Dominica":47,"Dominican Republic":1837,"Ecuador":19646,"Egypt":14151,"El Salvador":2496,"Equatorial Guinea":89,"Eritrea":74,"Estonia":1703,"Eswatini":1114,"Ethiopia":5008,"Falkland Islands (Malvinas)":0,"Faroe Islands":14,"Fiji":696,"Finland":1118,"France":56958,"French Guiana":268,"French Polynesia":522,"Gabon":224,"Gambia":219,"Georgia":11295,"Germany":68033,"Ghana":971,"Gibraltar":94,"Greece":15920,"Greenland":1,"Grenada":200,"Guadeloupe":676,"Guam":149,"Guatemala":11299,"Guernsey":8,"Guinea":310,"Guinea-Bissau":104,"Guyana":887,"Haiti":537,"Holy See":0,"Honduras":7323,"Hungary":29649,"Iceland":6,"India":332342,"Indonesia":121956,"Iran (Islamic Republic of)":76477,"Iraq":11346,"Ireland":3827,"Isle of Man":32,"Israel":4923,"Italy":63643,"Jamaica":2168,"Japan":14979,"Jersey":47,"Jordan":8805,"Kazakhstan":15478,"Kenya":3709,"Kiribati":0,"Kosovo[1]":1658,"Kuwait":1535,"Kyrgyzstan":1447,"Lao People's Democratic Republic":372,"Latvia":3935,"Lebanon":7659,"Lesotho":607,"Liberia":198,"Libya":4237,"Liechtenstein":25,"Lithuania":5597,"Luxembourg":413,"Madagascar":766,"Malawi":2166,"Malaysia":31024,"Maldives":214,"Mali":389,"Malta":258,"Marshall Islands":0,"Martinique":741,"Mauritania":523,"Mauritius":776,"Mayotte":130,"Mexico":156199,"Micronesia (Federated States of)":0,"Monaco":35,"Mongolia":1985,"Montenegro":1724,"Montserrat":0,"Morocco":7489,"Mozambique":1831,"Myanmar":16586,"Namibia":3437,"Nauru":0,"Nepal":8836,"Netherlands":9589,"New Caledonia":281,"New Zealand":26,"Nicaragua":52,"Niger":173,"Nigeria":1752,"Niue":0,"North Macedonia":5461,"Northern Mariana Islands (Commonwealth of the)":11,"Norway":958,"occupied Palestinian territory, including east Jerusalem":3431,"Oman":2986,"Other":0,"Pakistan":18874,"Palau":0,"Panama":3492,"Papua New Guinea":581,"Paraguay":14404,"Peru":109518,"Philippines":42274,"Pitcairn Islands":0,"Poland":68416,"Portugal":12095,"Puerto Rico":1643,"Qatar":372,"Republic of Korea":4725,"Republic of Moldova":7159,"RÃ©union":367,"Romania":43118,"Russian Federation":251841,"Rwanda":1263,"Saba":0,"Saint BarthÃ©lemy":4,"Saint Helena, Ascension and Tristan da Cunha":0,"Saint Kitts and Nevis":28,"Saint Lucia":290,"Saint Martin":27,"Saint Pierre and Miquelon":0,"Saint Vincent and the Grenadines":83,"Samoa":0,"San Marino":40,"Sao Tome and Principe":40,"Saudi Arabia":2661,"Senegal":1488,"Serbia":9525,"Seychelles":125,"Sierra Leone":47,"Singapore":799,"Sint Eustatius":0,"Sint Maarten":48,"Slovakia":14497,"Slovenia":3139,"Solomon Islands":0,"Somalia":1203,"South Africa":63028,"South Sudan":72,"Spain":37229,"Sri Lanka":14775,"Sudan":1776,"Suriname":1069,"Sweden":5639,"Switzerland":4393,"Syrian Arab Republic":2189,"Tajikistan":35,"Thailand":21637,"The United Kingdom":83496,"Timor-Leste":122,"Togo":180,"Tokelau":0,"Tonga":0,"Trinidad and Tobago":2699,"Tunisia":20944,"TÃ¼rkiye":61462,"Turkmenistan":0,"Turks and Caicos Islands":20,"Tuvalu":0,"Uganda":2993,"Ukraine":77366,"United Arab Emirates":1497,"United Republic of Tanzania":716,"United States of America":467051,"United States Virgin Islands":66,"Uruguay":6000,"Uzbekistan":871,"Vanuatu":0,"Venezuela (Bolivarian Republic of)":4300,"Viet Nam":32359,"Wallis and Futuna":7,"Yemen":1373,"Zambia":3344,"Zimbabwe":4637},
                    
                    "success":true,
                    "message":"Deaths by Year in all countries",
                    "Region":null,
                    "country":null,
                    "Year":2021}
    
    #### Example 7: [http://localhost:5000/deaths/?region=EMRO&country=Afghanistan](http://localhost:5000/deaths/?region=EMRO&country=Afghanistan)

    #### Response 7: 
                    {"data":{"Afghanistan":7922},
                      "success":true,
                      "message":"Deaths of Country in region",
                      "Region":"EMRO",
                      "country":"Afghanistan",
                      "Year":null}
6. The "/cases/" route is similar to the "/deaths/" route but focuses on retrieving case information.
7. The "/max_deaths/" route returns the country with the maximum number of deaths.

    #### Example 8: http://localhost:5000/max_deaths/

    #### Response 8:
                    {"data":"occupied Palestinian territory, including east Jerusalem",
                    "success":true,
                    "message":"Maximum deaths by Country",
                    "size":237}
    
   
8. The "/max_deaths_with_in_date_range/" route returns the maximum deaths within a specified date range. It accepts parameters for minimum and maximum dates.
9. The "/min_deaths/" route returns the country with the minimum number of deaths.

    #### Example 9:[http://localhost:5000/min_deaths/](http://localhost:5000/min_deaths/)

    #### Response 9:
                    {"data":"Afghanistan",
                    "success":true,
                    "message":"Minimum deaths by Country",
                    "size":237}

   
10. The "/avg_deaths/" route returns the country with the average number of deaths by country.
    
    #### Example 10: [http://localhost:5000/avg_deaths/](http://localhost:5000/avg_deaths/)

    #### Response 10: 
                {"data":29306,
                "success":true,
                "message":"Average deaths by Country",
                "size":237}
    
   

Overall, this code demonstrates the use of FastAPI to create a web API for accessing and analyzing COVID-19 data. It leverages CSV data and provides flexible filtering options for retrieving specific information. The routes and their respective responses facilitate easy access to COVID-19 statistics based on various criteria.

### Deliverables

|  #  | File Name                | Description                       |
| :-: | :----------------        | :-------------------------------- |
|  1  | [api.py](api.py)         | This Python file implements a FastAPI web application for retrieving and analyzing COVID-19 data from a CSV file.      |
|  2  | [data.csv](data.csv)     | The "data.csv" file contains COVID-19 data including cases, deaths, countries, WHO regions, and other related information.    |

