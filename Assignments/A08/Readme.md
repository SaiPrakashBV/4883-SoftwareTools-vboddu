## Assignment 8 - Fast Api with Covid Data

### Venkata Sai Prakash Boddu

### Overview:

Creating a RESTful API using FastAPI that provides access to COVID-19 data. The API will fetch the data from a publicly available data source and expose endpoints to retrieve various statistics related to COVID-19 cases.

### Data File

The data is provided here: [data.csv](data.csv)

Column Descriptions:

|  #  | Column            | Description                       |
| :-: | :---------------- | :-------------------------------- |
|  0  | Date_reported     | date in `yyyy-mm-dd` format       |
|  1  | Country_code      | A unique 2 digit country code     |
|  2  | Country           | Name of the country               |
|  3  | WHO_region        | World Health Organization region  |
|  4  | New_cases         | Number of new cases on this date  |
|  5  | Cumulative_cases  | Cumulative cases up to this date  |
|  6  | New_deaths        | Number of new deaths on this date |
|  7  | Cumulative_deaths | Cumulative deaths up to this date |
