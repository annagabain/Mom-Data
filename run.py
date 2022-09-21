import pandas as pd

def main():
    """
    Runs when the programme starts
    """
    print(f"\n...............Hello and welcome to MOM DATA...............\n")
    print(f"...Here you can get insights about your monthly expenses...\n")


main()

print("Type ADD to add new data or VIEW to see the year's overview")
decision_one = input().upper()
if decision_one == 'VIEW':
    # Read the Expenses file with help of Pandas library
    df = pd.read_excel (r'Expenses.xlsx')
    print (f"OVERVIEW 2022: \n \n {df}")
elif decision_one == 'ADD':
    print ("Insert 4 numbers, separated by commas for Food, Transport, Accomodation, Clothing")
else:
    print("Try again")


