import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('mom_expenses')

# Open a sheet from a google API spreadsheet
# sheet = service_account.open("mom_expenses")
standard_worksheet = SHEET.worksheet("standard")

def intro_title():
    """
    Runs when the programme starts
    """
    print(f"\n=========   Hello and welcome to MOM DATA   =========\n")
    print(f"Here you can get insights about your monthly expenses\n")
    print(f"=====================================================\n")
    print()
    main_menu()


def main_menu():
    """
    Enables the user's first decision making: 
    input to add new expenses or to view the existing expenses
    """
    while True:
        print("Please type... \n")
        decision_one = input("- ADD to add new expenses \n- VIEW to see the year's overview or \n- EXIT to exit the programme: \n\n").upper()
        if decision_one == 'EXIT':
            print("Goodbye!")
            exit()
        elif decision_one == 'VIEW':
            view_expenses()
        elif decision_one == 'ADD':
            update_expenses()
        else:
            print("Invalid input, please try again: \n")
            main_menu()


def add_new_expenses():
    """
    Collect the 'standard' expenses data from the user
    """
    worksheet = SHEET.worksheet("standard")   

    # individual rows to update or add new expenses to
    January = worksheet.row_values(3)
    February = worksheet.row_values(4)
    March = worksheet.row_values(5)
    April = worksheet.row_values(6)
    May = worksheet.row_values(7)
    June = worksheet.row_values(8)

    #Choose the expense month...
    decision_two = input("\n Choose the expense month...\n- 1 January\n- 2 February\n- 3 March\n- 4 April\n- 5 May\n- 6 June\n")
    
    if decision_two == "1":
        print(January)
    elif decision_two == "2":
        print(February)
    elif decision_two == "3":
        print(March)
    elif decision_two == "4":
        print(April)
    elif decision_two == "5":
        print(May)
    elif decision_two == "6":
        print(June)
    else:
        print("try again..")

    #...add expenses to it or overwrite if exists
    print(worksheet.find("January"))
    
    # user_input_one = input("Insert **1 month and** 4 numbers, separated by commas for Food, Transport, Accomodation, Clothing: \n" )
    # input_one_columns = user_input_one.split(",")
    # return input_one_columns


def update_expenses():
    """
    Update the Standard Expenses sheet with the data from the add_new_expenses
    """
    worksheet_to_update = SHEET.worksheet("standard")

    # write to the 'standard' expenses data from google  API spreadsheet
    # worksheet_to_update.append_row(add_new_expenses())

    #test to update one sell
    worksheet_to_update.update('B3', '1150')

    print(f"Expenses updated successfully.\n")

    main_menu()


def view_expenses():
    """
    View the existing expenses
    """   
    # my 'standard' expenses data from google  API spreadsheet
    print("-----------------------------------------------------")
    print(f"Year's Expenses overview:\n ")
    print("-----------------------------------------------------")
    dataframe = pd.DataFrame(standard_worksheet.get_all_records())
    print(dataframe)
    print("-----------------------------------------------------")

    print()


intro_title()
