import pandas as pd
# import gspread
# from google.oauth2.service_account import Credentials


# service_account = gspread.service_account(filename="service_account.json")
# CREDS = Credentials.from_service_account_file('service_account.json')

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

def main():
    """
    Runs when the programme starts
    """
    print(f"\n=========   Hello and welcome to MOM DATA   =========\n")
    print(f"Here you can get insights about your monthly expenses\n")
    print(f"=====================================================\n")
    print()

    add_or_view()


def add_or_view():
    """
    Enables the user's first decision making: 
    input to add new expenses or to view the existing expenses
    """
    while True:
        print("Type: \n")
        decision_one = input("- ADD to add new data \n- VIEW to see the year's overview or \n- EXIT to exit the programme: \n\n").upper()
        if decision_one == 'EXIT':
            break
        elif decision_one == 'VIEW':
            view_expenses()
        elif decision_one == 'ADD':
            add_expenses()
        else:
            print("Invalid input, try again: \n")
            add_or_view()


def add_user_input():
    """
    Collect the 'standard' expenses data from the user
    """
    user_input_one = input("Insert 1 month and 4 numbers, separated by commas for Food, Transport, Accomodation, Clothing: \n" )
    input_one_columns = user_input_one.split(",")
    return input_one_columns


def add_expenses():
    """
    Update the Standard Expenses sheet with the data from the user_input_one
    """
    worksheet_to_update = SHEET.worksheet("standard")

    #Choose the expense month, add expenses to it or overwrite if exists
    #THE CODE GOES HERE
    
    # write to the 'standard' expenses data from google  API spreadsheet
    worksheet_to_update.append_row(add_user_input())
    print(f"Expenses updated successfully.\n")

    add_or_view()


def view_expenses():
    """
    View the existing expenses
    """   
    # my 'standard' expenses data from google  API spreadsheet
    print(f"Year's Expenses overview:\n ")
    dataframe = pd.DataFrame(standard_worksheet.get_all_records())
    print(dataframe)


main()
