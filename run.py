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
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]


def print_months():
    """
    Print the months for the choose_month_menu
    """
    i = 1
    for month in months:
        print(f"- {i} - for {month}")
        i += 1


def set_budget():
    """
    Setting the monthly budget
    """
    while True:
        print(f"Please set a Budget for {months[int(MONTH_NUMBER) -1 ]},")
        global BUDGET
        BUDGET = input("e.g. 2500...\n\n")
        print()
        try:
            BUDGET = int(BUDGET)
            print(f"Your budget of {BUDGET} is confirmed")
            print()
            print()
        except ValueError:
            print(f"{BUDGET} is not a valid budget")
            print('Make sure you entered a number!')
            print()
            print("Try again...")
            continue
        return False
    return BUDGET


def main_menu():
    """
    Enables the user's first decision making:
    input to add new expenses or to view the existing expenses
    """
    while True:
        print("Please type... \n")
        print("     - (V)IEW - to see the year's overview")
        print("     - (A)DD - to add new expenses")
        print("     - (E)XIT - to exit the programme")
        
        menu_input = input().upper()
        if menu_input == 'E':
            print("Goodbye!")
            exit()
        elif menu_input == 'V':
            view_expenses()
        elif menu_input == 'A':
            update_expenses()
        else:
            print("Invalid input, please try again: \n")
            main_menu()


def intro_title():
    """
    Runs when the programme starts
    """
    print("\n  =========   Hello and welcome to MOM DATA   =========\n")
    print("  Here you can get insights about your monthly expenses\n")
    print("  =====================================================\n")
    print()

    main_menu()


def choose_month_menu():
    """
    Choose the month and locate the row that will be updated
    """
    worksheet = SHEET.worksheet("standard")
    while True:
        print("\nChoose the expense month,\ntype numbers 1 to 12...\n")
        print_months()
        print()
        global MONTH_NUMBER
        MONTH_NUMBER = input()
        print()

        try:
            MONTH_NUMBER = int(MONTH_NUMBER)
        except ValueError:
            print(f"{MONTH_NUMBER} is not a number")
            print('Make sure you entered a number!')
            print("Try again...")
            print()
            continue

        if int(MONTH_NUMBER) < 1 or int(MONTH_NUMBER) > 12:
            print(f"There is no month for number:  {MONTH_NUMBER}")
            print("Try again...")
            continue

        result = worksheet.find(months[int(MONTH_NUMBER)-1])
        print(f"Chosen month: {months[int(MONTH_NUMBER) -1 ]}\n")
        set_budget()

        return f"B{result.row}:E{result.row}"


def locate_the_budget_status_cell():
    """
    Locate the budget status (budget-sum) cell 
    for the month that will be updated
    """
    result = standard_worksheet.find(months[int(MONTH_NUMBER)-1])
    return f"H{result.row}"


def locate_the_budget_cell():
    """
    Locate the budget cell for the month that will be updated
    """
    result = standard_worksheet.find(months[int(MONTH_NUMBER)-1])
    return f"G{result.row}"


def locate_the_sum_cell():
    """
    Finds the F cell of the corresponding month row
    """
    monthly_sum_cell = standard_worksheet.find(months[int(MONTH_NUMBER)-1])
    return f"F{monthly_sum_cell.row}"


def update_monthly_sum():
    """
    Finds all the expense values of the corresponding month and adds them up
    """
    print("Updating this month's sum...")

    result = standard_worksheet.find(months[int(MONTH_NUMBER)-1])
    # Find indicidual cells
    cell_one = f"B{result.row}"
    cell_two = f"C{result.row}"
    cell_three = f"D{result.row}"
    cell_four = f"E{result.row}"

    val_one = standard_worksheet.acell(cell_one).value
    val_two = standard_worksheet.acell(cell_two).value
    val_three = standard_worksheet.acell(cell_three).value
    val_four = standard_worksheet.acell(cell_four).value

    month_sum = int(val_one) + int(val_two) + int(val_three) + int(val_four)

    sum_cell = locate_the_sum_cell()
    standard_worksheet.update(sum_cell, month_sum)

    return month_sum


def update_budget_status():
    """
    Updates the budget status, that is a result of the difference between
    the given budget and the sum of all expenses during the given month
    """
    print("Updating the budget status...")
    monthly_sum = update_monthly_sum()
    budget_status = BUDGET - monthly_sum

    budget_status_cell = str(locate_the_budget_status_cell())
    budget_cell = str(locate_the_budget_cell())
    
    standard_worksheet.update(budget_status_cell, budget_status)
    standard_worksheet.update(budget_cell, BUDGET)

    return budget_status


def update_expenses():
    """
    Collect the 'standard' expenses data from the user
    Validate the input
    Update the Standard Expenses sheet cells retrieved 
    from locate_the_month_row function
    """
    cells = str(choose_month_menu())
    worksheet = SHEET.worksheet("standard")

    # Updating specific row from user input
    while True:
        print("Insert 4 numbers, separated by commas,")
        print("for Food, Transport, Accomodation, Clothing... \n")

        four_expense_values = input()
        try:
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
        print("Updating expenses...")
        worksheet.update(cells, [input_two])
        update_budget_status()
        print("Expenses updated successfully.\n")
        main_menu()


def view_expenses():
    """
    View the existing expenses at google  API spreadsheet
    """
    print()
    print("------------------------------------------------------------------")
    print("    Year's Expenses overview: ")
    print("------------------------------------------------------------------")
    dataframe = pd.DataFrame(standard_worksheet.get_all_records())
    print(dataframe.to_string(index=False))
    print("------------------------------------------------------------------")

    print()


intro_title()
