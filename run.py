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

CREDS = Credentials.from_service_account_file('service_account.json')
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
    print(f"\n...............Hello and welcome to MOM DATA...............\n")
    print(f"...Here you can get insights about your monthly expenses...\n")

    add_or_view()


def add_or_view():
    """
    Enables the user's first decision making: 
    input to add new expenses or to view the existing expenses
    """
    decision_one = input("Type ADD to add new data or VIEW to see the year's overview: \n\n").upper()
    if decision_one == 'VIEW':
        view_expenses()
    elif decision_one == 'ADD':
        add_expenses()
    else:
        print("Invalid input, try again: \n")
        add_or_view()

def add_expenses():
    """
    Update the expenses(test) with the data from input
    """
    print ("Insert 4 numbers, separated by commas for Food, Transport, Accomodation, Clothing")
    f = open("test_expenses.txt", "a")
    f.write(input())
    f.write("\n")
    print(f"Updating expenses...\n")
    f.close()
    print(f"Expenses updated successfully.\n")

    add_or_view()


def view_expenses():
    """
    View the existing expenses
    """   
    #data from google spreadsheet API
    print(f"Year's overview data:\n ")
    dataframe = pd.DataFrame(standard_worksheet.get_all_records())
    print(dataframe)


main()
