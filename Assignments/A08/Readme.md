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
6. The "/cases/" route is similar to the "/deaths/" route but focuses on retrieving case information.
7. The "/max_deaths/" route returns the country with the maximum number of deaths.
8. The "/max_deaths_with_in_date_range/" route returns the maximum deaths within a specified date range. It accepts parameters for minimum and maximum dates.
9. The "/min_deaths/" route returns the country with the minimum number of deaths.
10. The "/avg_deaths/" route returns the country with the average number of deaths by country.

Overall, this code demonstrates the use of FastAPI to create a web API for accessing and analyzing COVID-19 data. It leverages CSV data and provides flexible filtering options for retrieving specific information. The routes and their respective responses facilitate easy access to COVID-19 statistics based on various criteria.

### Deliverables

|  #  | File Name                | Description                       |
| :-: | :----------------        | :-------------------------------- |
|  1  | [api.py](api.py)         | This Python file implements a FastAPI web application for retrieving and analyzing COVID-19 data from a CSV file.      |
|  2  | [data.csv](data.csv)     | The "data.csv" file contains COVID-19 data including cases, deaths, countries, WHO regions, and other related information.    |

