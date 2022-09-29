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
standard_worksheet = SHEET.worksheet("standard")
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


def set_budget():
    """
    Setting the monthly budget
    """
    while True:
        print("Please set a Budget\n")
        global budget 
        budget = input("     e.g. 2500...\n\n")
        print()
        try:
            budget = int(budget)
            print(f"Your budget of {budget} is confirmed")
            print()
            print()
        except ValueError:
            print(f"{budget} is not a valid budget")
            print('Make sure you entered a number!')
            print()
            print("Try again...")
            continue
            print()
        return False
    return budget

def main_menu():
    """
    Enables the user's first decision making: 
    input to add new expenses or to view the existing expenses
    """
    while True:
        print("Please type... \n")
        decision_one = input("     - VIEW - to see the year's overview \n     - ADD - to add new expenses or \n     - BUDGET - to change the budget or \n     - EXIT - to exit the programme: \n\n").upper()
        if decision_one == 'EXIT':
            # share()
            print("Goodbye!")
            exit()
        elif decision_one == 'VIEW':
            view_expenses()
        elif decision_one == 'BUDGET':
            set_budget()
        elif decision_one == 'ADD':
            update_expenses()
        else:
            print("Invalid input, please try again: \n")
            main_menu()
    

def intro_title():
    """
    Runs when the programme starts
    """
    print(f"\n=========   Hello and welcome to MOM DATA   =========\n")
    print(f"Here you can get insights about your monthly expenses\n")
    print(f"=====================================================\n")
    print()

    set_budget()
    main_menu()


def share():
    """
    Share the worksheet with the user
    """
    SHEET.share('user@example.com', perm_type='user', role='writer')
    print(f"Shared successfully.\n")


def locate_the_month_row():
    """
    Choose the month and locate the row that will be updated
    """
    worksheet = SHEET.worksheet("standard")   
    
    while True:
        
        # Choose the expense month...
        print("\nChoose the expense month,\ntype numbers 1 to 12...\n")
        global month_number
        month_number = input("     - 1  - for January\n     - 2  - for February\n     - 3  - for March\n     - 4  - for April\n     - 5  - for May\n     - 6  - for June\n     - 7  - for July\n     - 8  - for August\n     - 9  - for September\n     - 10 - for October\n     - 11 - for November\n     - 12 - for December\n\n")
        print()

        try:
            month_number = int(month_number)
        except ValueError:
            print(f"{month_number} is not a number")
            print('Make sure you entered a number!')
            print()
            print("Try again...")
            print()
            continue
        
        result = worksheet.find(months[int(month_number)-1])
        print(f"Chosen month: {months[int(month_number) -1 ]}\n")
        return f"B{result.row}:E{result.row}"


def locate_the_budget_status_cell():
    """
    Locate the budget status cell for the month that will be updated
    """
    
    result = standard_worksheet.find(months[int(month_number)-1])
    print(f"Chosen month: {months[int(month_number) -1 ]}\n")
    return f"F{result.row}"

def update_total():
    print("Updating total...")

def update_budget_status():
    print("Updating the budget status...")
    #budget - sum to identify budget status
    budget_status = budget - 100

    cell = str(locate_the_budget_status_cell())
   

    # standard_worksheet.update(cells, [budget_status])
    standard_worksheet.update(cell, budget_status)

    return budget_status


def update_expenses():
    """
    Collect the 'standard' expenses data from the user
    Validate the input
    Update the Standard Expenses sheet cells retrieved from locate_the_month_row function
    """
    cells = str(locate_the_month_row())
    worksheet = SHEET.worksheet("standard")

    # Updating specific row from user input
    while True:
        four_expense_values = input("Insert 4 numbers, separated by commas,\n for Food, Transport, Accomodation, Clothing... \n" )
        try:
            # four_expense_values = int(four_expense_values)
            input_two = four_expense_values.split(",")

            if len(input_two) != 4:
                raise ValueError()

            def expense():
                for expense in input_two:
                    expense = int(expense)
            expense()
                
        except ValueError:
            print('Make sure you entered ONLY numbers (exactly 4 of them)!')
            print("Try again...")
            print()
            continue
    
        # write to the 'standard' expenses data from google  API spreadsheet
        print(f"Updating expenses...")
        worksheet.update(cells, [input_two])
        update_total()
        update_budget_status()
        print(f"Expenses updated successfully.\n")

        return False
    
    main_menu()


def view_expenses():
    """
    View the existing expenses
    """   
    # my 'standard' expenses data from google  API spreadsheet
    print()
    print("-------------------------------------------------------------")
    print(f"Year's Expenses overview:\n ")
    print("-------------------------------------------------------------")
    dataframe = pd.DataFrame(standard_worksheet.get_all_records())
    print(dataframe.to_string(index=False))
    print("-------------------------------------------------------------")

    print()


intro_title()
