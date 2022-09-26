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
        decision_one = input("- VIEW to see the year's overview \n- ADD to add new expenses or \n- EXIT to exit the programme: \n\n").upper()
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


def locate_the_month_row():
    """
    Choose the month and locate the row that will be updated
    """
    worksheet = SHEET.worksheet("standard")   
    
    #Choose the expense month...
    print("\nChoose the expense month,\ntype numbers 1 to 12...\n")
    month_number = input("- 1 January\n- 2 February\n- 3 March\n- 4 April\n- 5 May\n- 6 June\n- 7 July\n- 8 August\n- 9 September\n- 10 October\n- 11 November\n- 12 December\n\n")
    print()
    # individual rows to update or add new expenses to
    # January = worksheet.row_values(3)
    # February = worksheet.row_values(4)
    # March = worksheet.row_values(5)
    # April = worksheet.row_values(6)
    # May = worksheet.row_values(7)
    # June = worksheet.row_values(8)

    if month_number == "1":
        month_row = 'B3:E3'
        month = 'January'
    elif month_number == "2":
        month_row = 'B4:E4'
        month = 'February'
    elif month_number == "3":
        month_row = 'B5:E5'
        month = 'March'
    elif month_number == "4":
        month_row = 'B6:E6'
        month = 'April'
    elif month_number == "5":
        month_row = 'B7:E7'
        month = 'May'
    elif month_number == "6":
        month_row = 'B8:E8'
        month = 'June'
    elif month_number == "7":
        month_row = 'B9:E9'
        month = 'July'
    elif month_number == "8":
        month_row = 'B10:E10'
        month = 'August'
    elif month_number == "9":
        month_row = 'B11:E11'
        month = 'September'
    elif month_number == "10":
        month_row = 'B12:E12'
        month = 'October'
    elif month_number == "11":
        month_row = 'B13:E13'
        month = 'November'
    elif month_number == "12":
        month_row = 'B14:E14'
        month = 'December'
    else:
        print("try again..")

    print(f"Chosen month: {month}\n")

    return month_row


# Print the specific month row item(s)
# new_list = []
# for item in month_row:
#     new_list.append(item)
# values_without_month_name = new_list[1:]
# print(f"{new_list[0]} values {values_without_month_name}")

# TO DO!
    #...add expenses to it or overwrite if exists
    # print(worksheet.find("January"))

def update_expenses():
    """
    Collect the 'standard' expenses data from the user
    Update the Standard Expenses sheet cells retrieved from locate_the_month_row function
    """
    cells = str(locate_the_month_row())
    
    # write to the 'standard' expenses data from google  API spreadsheet
    worksheet = SHEET.worksheet("standard")

    #test updating specific row from user input
    user_input_two = input("Insert 4 numbers, separated by commas,\n for Food, Transport, Accomodation, Clothing... \n" )
    input_two = user_input_two.split(",")
    worksheet.update(cells, [input_two])
    print(f"Expenses updated successfully.\n")

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
