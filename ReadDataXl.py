from openpyxl import load_workbook

workbook = load_workbook("employees.xlsx")

sheet = workbook.active

print(sheet["A2"].value)
print(sheet["B2"].value)