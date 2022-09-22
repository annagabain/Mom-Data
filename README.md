# Mom Data
## Budget Analysing Tool for the Whole Family

The application creates and populates a database from user input
It's possible to sort data by headings (and filter by budget)
Budgeting suggestions are given based on headings chosen

<img width="100%" alt="I am responsive mom lifehacks media sizes" src="assets/initial_scribble_1.jpg">
<img width="100%" alt="I am responsive mom lifehacks media sizes" src="assets/initial_scribble_2.jpg">

### Structure Flowchart

<img width="100%" alt="I am responsive mom lifehacks media sizes" src="assets/Mom_Data_Lucidchart.png">

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

### Sources
How to use Pandas: https://datatofish.com/read_excel/

How to Use Google Sheets With Python (2022): https://www.youtube.com/watch?v=bu5wXjz2KvU