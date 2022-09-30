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

<img width="100%" alt="mom data" src="assets/initial_scribble_2.jpg">
<img width="50%" alt="Mom Data Initial Structure Flowchart" src="assets/Mom_Data_Lucidchart_old.png">

## Testing

No automated testing has been used on this project, i have opted to do all testing manually and through numerous user experiences.

Method:
Test:
Resullt:

### Validators

PEP8

<img width="100%" alt="screenshot with PEP8 issue" src="assets/pep_issue.jpg">

<img width="100%" alt="screenshot with PEP8 problems" src="assets/pep8_check.jpg">


### Manual testing

<img width="100%" alt="testing in the terminal" src="assets/manual_testing.jpg">

### Debugging

Bug:
Cause:
Solution:

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

Playing on a Local machine or via Gitpod Terminal:

This project was developed by forking a specialized Code Institute template which simulates a terminal in the web browser. Due to this, I optimized the game to work via the final Heroku deployment, and I do not recommend playing it locally. That said, I have included this section to give you a choice.

    Navigate to the GitHub repository, and follow these steps to clone the project into your IDE of choice.
        Gitpod only requires you to have the web extension installed and click the green Gitpod button from the repositories main page. If you are using Gitpod please skip step 2 below as you do not require a virtual environment to protect your machine.

    Create the virtual environment with the terminal command "python3 -m venv venv". Once complete add the "venv" file to you're ".gitignore" file and use the terminal command "venv\Scripts\activate.bat" to activate it.
        IMPORTANT If developing locally on your device, ensure you set up/activate the virtual environment before installing/generating the requirements.txt file; failure to do this will pollute your machine and put other projects at

    Install the requirements listed in requirements.txt using the terminal command "pip3 install -r requirements.txt"
        Kindly note that since I developed the project from scratch and installed the required libraries as progressed I have already included a requirements.txt for this app by using the terminal command "pip3 freeze > requirements.txt" to generate it.

Final Deployment to Heroku:

The project was deployed to Heroku using the below procedure:-

    Log in to Heroku or create an account if required.
    click the button labeled New from the dashboard in the top right corner, just below the header.
    From the drop-down menu select "Create new app".
    Enter a unique app name. I combined my GitHub user name and the game's name with a dash between them (dnlbowers-battleship) for this project.
    Once the web portal shows the green tick to confirm the name is original select the relevant region. In my case, I chose Europe as I am in Malta.
    When happy with your choice of name and that the correct region is selected, click on the "Create app" button.
    This will bring you to the project "Deploy" tab. From here, navigate to the settings tab and scroll down to the "Config Vars" section.
    Click the button labelled "Reveal Config Vars" and enter the "key" as port, the "value" as 8000 and click the "add" button.
    Scroll down to the buildpacks section of the settings page and click the button labeled " add buildpack," select "Python," and click "Save Changes".
    Repeat step 11 but this time add "node.js" instead of python.
        IMPORTANT The buildpacks must be in the correct order. If node.js is listed first under this section, you can click on python and drag it upwards to change it to the first buildpack in the list.
    Scroll back to the top of the settings page, and navigate to the "Deploy" tab.
    From the deploy tab select Github as the deployment method.
    Confirm you want to connect to GitHub.
    Search for the repository name and click the connect button next to the intended repository.
    From the bottom of the deploy page select your preferred deployment type by follow one of the below steps:
        Clicking either "Enable Automatic Deploys" for automatic deployment when you push updates to Github.
        Select the correct branch for deployment from the drop-down menu and click the "Deploy Branch" button for manual deployment.


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