import pandas as pd


# reading the csv file
csv_file = pd.read_csv("manual_testing.csv")

# creating an output excel file
excel_file = pd.ExcelWriter("manual_testing.xlsx")

# converting the csv file to excel file
csv_file.to_excel(excel_file, index=False)

# closing the file
excel_file.save()

