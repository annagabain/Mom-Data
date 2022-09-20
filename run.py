import pandas as pd

def main():
    """
    Runs when the programme starts
    """
    print(f"\n...............Hello and welcome to MOM DATA...............\n")
    print(f"...Here you can get insights about your monthly expenses...\n")


main()


# Read the Expenses file with help of Pandas library
df = pd.read_excel (r'Expenses.xlsx')
print (f"OVERVIEW 2022: \n \n {df}")
