## How does it work?

For this project you need to do:
- Create a venv;
- Create a folder called data_files in the root;
- Create .env file


#### Create a venv
There are many ways to create a venv, depending on whether you are using Windows, Mac or Linux. I recommend you to look in python documentation: 
https://docs.python.org/3/library/venv.html

If you are using Windows and never create a venv, you will probably need run this code in the PowerShell:

        PS C:> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
This code will permite you activate the venv. On the documentation that are cited previously had an explanation for this.

#### Create a folder called data_files
Resultados de tradução
This project was built from files I found on Kaggle. There are data from 4 streaming videos (disney+, hbo max, netflix and prime video). You will need create a folder structure like this:

- data_files
    - disney_plus
        - credits.csv
        - titles.csv

Replicate this structure for the others one streamings.

> disney: https://www.kaggle.com/datasets/shivamb/disney-movies-and-tv-shows
> hbo: https://www.kaggle.com/datasets/victorsoeiro/hbo-max-tv-shows-and-movies
> netflix: https://www.kaggle.com/datasets/shivamb/netflix-shows
> prime video: https://www.kaggle.com/datasets/victorsoeiro/amazon-prime-tv-shows-and-movies

<img src="https://img.shields.io/badge/last%20modified-today-brightgreen" alt="Power BI" width="30" height="30"/>

#### Create a .env file
If you don't know what it is a .env file I recommend this page:
https://towardsdatascience.com/the-quick-guide-to-using-environment-variables-in-python-d4ec9291619e

This file has secret information like user, passwords and database host. This information cannot be uploaded to github, so we will use this file to configure your environment.

I'm using a localhost express SQL Server.

        DEBUG=true
        DRIVER_SQL=DRIVER SQL
        SERVER_SQL=ENDPOINT
        DATABASE_SQL=DATABASE

### Disclaimer

This project are developed as my portfolio. I want to include some features: automated tests with PyTest, DW Modeling and a Dashboard for analysis.

<img src="https://img.shields.io/badge/last%20modified-today-brightgreen" alt="Power BI" width="30" height="30"/>