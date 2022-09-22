import pandas as pd

def main():
    """
    Runs when the programme starts
    """
    print(f"\n...............Hello and welcome to MOM DATA...............\n")
    print(f"...Here you can get insights about your monthly expenses...\n")

    add_or_view()


def add_or_view():
    print("Type ADD to add new data or VIEW to see the year's overview")
    decision_one = input().upper()
    if decision_one == 'VIEW':
        view_expenses()
    elif decision_one == 'ADD':
        add_expenses()
    else:
        print("Invalid input, try again: ")
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
    View the existing expenses(test)
    """   
    #  # Read the Expenses file with help of Pandas library (testing desired view)
    # df = pd.read_excel (r'Expenses.xlsx')
    # print (f"OVERVIEW 2022: \n \n {df}")

    # Read the expenses(test), a file that actually stores the current added input

    f = open("test_expenses.txt", "r")
    print(f.read())


main()
