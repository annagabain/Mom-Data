# Mom Data
## Budget Analysing Tool for the Whole Family

Mom Data is a user-freindly application for storing, retrieveing and calculating major life expense categories: Food, Transport, Accomodation and Clothing. Mom Data is for family budget keepers. It aims to provide a clear overview on their monthly expenses thorough the year. 

The application populates a database from user input, calculates the sum of the monthly expenses and compares it to the given budget. It gives a clear user guidance and feedback about the inputs, checks the data to be valid and that the programme flows uninterupted until the user choses to end it.

This is the third Portfolio Project in frames of Code Institute Full Stack Web Developer Course Assessment. It is for educational purposes, is developed in Python programming language, that runs in a command-line terminal that is visually presented through the Heroku platform. Further tools and languages will be implemented for the consequent projects.

:point_down: Click the link below for the live view: 

# [Live View](https://mom-data.herokuapp.com/)

<img width="100%" alt="I am responsive mom data media sizes" src="assets/am_i_responsive_no_mobile.jpg">


## Contents:
- [Features](#features)
    - [Future Features](#future-features)
- [Development Stages](#development-stages)
    - [Structure](#structure-flowchart)
    - [Planning](#initial-planning)
- [Testing](#testing)
    - [Validators](#validators)
    - [Manual Testing](#manual-testing)
    - [Debugging](#debugging)
- [Deployment](#deployment)
- [Sources & Credits](#sources-and-credits)
- [Acknowledgemts](#acknowledgements)

## Features
- Welcoming introduction

<img width="100%" alt="Main Menu" src="assets/main_menu.jpg">

- Main menu
    - VIEW
    - ADD
    - EXIT

- View the year's overview

<img width="100%" alt="expenses table" src="assets/view.jpg">

- Add monthly expenses for a specific month (choose from the menu), if existing, update data for that month

- Cat is not a number! ... User input validation


<img width="50%" alt="cat is not a number" src="assets/user_input_test_nan.jpg">

### Future Features:

- Each user should be able to create their own worksheet, with some pre-populated data to edit
- additional to standard expenses, custom categories can be added. Standard categories can be edited or removed
- Downloading and saving the current data possible

<img width="100%" alt="cat is not a number" src="assets/future_features_1.jpg">


## Development Stages

### Structure

<img width="50%" alt="Mom Data Structure" src="assets/structure.jpg">

<img width="100%" alt="Mom Data Structure Flowchart" src="assets/mom_data_lucidchart_final.png">


### Initial planning

<img width="50%" alt="mom data" src="assets/initial_scribble_1.jpg">
<img width="100%" alt="mom data" src="assets/initial_scribble_2.jpg">
<img width="50%" alt="Mom Data Initial Structure Flowchart" src="assets/Mom_Data_Lucidchart_old.png">

## Testing

### Validators

### Manual testing

<img width="100%" alt="testing in the terminal" src="assets/manual_testing.jpg">

### Debugging

Traceback error in the terminal

<img width="100%" alt="bug months" src="assets/bug_months.jpg">

Months menu bug

<img width="100%" alt="bug" src="assets/bug_month_number.jpg">

<img width="100%" alt="bug" src="assets/bug_month_number_fixed.jpg">



F-string bugs

<img width="100%" alt="bug" src="assets/bug_f_string.jpg">

Budget bug

<img width="100%" alt="bug" src="assets/bug_budget.jpg">

## Deployment

### Creating the Heroku app

Connected to GitHub repository and deployed.

## Sources and Credits

How to use Pandas: https://datatofish.com/read_excel/

How to Use Google Sheets With Python (2022): https://www.youtube.com/watch?v=bu5wXjz2KvU

Gspread for the project: https://github.com/annagabain/love-sandwiches-walkthrough from Code Institute

Some inspiration from Build A Simple Expense Tracker Using Python: https://www.youtube.com/watch?v=AnKc74fWYCg

How to Validate User Inputs in Python: https://www.youtube.com/watch?v=LUWyA3m_-r0

Global variables: https://www.w3schools.com/python/python_variables_global.asp

Flowchart: https://lucid.app/

## Acknowledgemts

Richard Wells - course mentor for friendly guidance, help with refactoring some code and feedback on the project

Jakob Lövhall - providing warm support, inculding babysitting most evenings to allow more time for the project