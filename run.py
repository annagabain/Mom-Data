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

def share():
    """
    Share the worksheet with the user
    """
    SHEET.share('user@example.com', perm_type='user', role='writer')
    print(f"Shared successfully.\n")

def main_menu():
    """
    Enables the user's first decision making: 
    input to add new expenses or to view the existing expenses
    """
    while True:
        print("Please type... \n")
        decision_one = input("- VIEW to see the year's overview \n- ADD to add new expenses or \n- EXIT to exit the programme: \n\n").upper()
        if decision_one == 'EXIT':
            # share()
            print("Goodbye!")
            exit()
        elif decision_one == 'VIEW':
            view_expenses()
        elif decision_one == 'ADD':
            update_expenses()
        else:
            print("Invalid input, please try again: \n")
            main_menu()

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    

def locate_the_month_row():
    """
    Choose the month and locate the row that will be updated
    """
    worksheet = SHEET.worksheet("standard")   
    
    #Choose the expense month...
    print("\nChoose the expense month,\ntype numbers 1 to 12...\n")
    month_number = input("- 1 January\n- 2 February\n- 3 March\n- 4 April\n- 5 May\n- 6 June\n- 7 July\n- 8 August\n- 9 September\n- 10 October\n- 11 November\n- 12 December\n\n")
    print()

    result = worksheet.find(months[int(month_number)-1])
    print(f"Chosen month: {months[int(month_number) -1 ]}\n")

    return f"B{result.row}:E{result.row}"


def update_expenses():
    """
    Collect the 'standard' expenses data from the user
    Validate the input
    Update the Standard Expenses sheet cells retrieved from locate_the_month_row function
    """
    cells = str(locate_the_month_row())
    worksheet = SHEET.worksheet("standard")

    #Updating specific row from user input
    while True:
        user_input_two = input("Insert 4 numbers, separated by commas,\n for Food, Transport, Accomodation, Clothing... \n" )
        try:
            # user_input_two = int(user_input_two)
            input_two = user_input_two.split(",")

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
        print(f"Updating expenses...\n")
        worksheet.update(cells, [input_two])
        print(f"Expenses updated successfully.\n")
        return False
    
    main_menu()


def view_expenses():
    """
    View the existing expenses
    """   
    # my 'standard' expenses data from google  API spreadsheet
    print()
    print("-----------------------------------------------------")
    print(f"Year's Expenses overview:\n ")
    print("-----------------------------------------------------")
    dataframe = pd.DataFrame(standard_worksheet.get_all_records())
    print(dataframe)
    print("-----------------------------------------------------")

    print()


intro_title()

