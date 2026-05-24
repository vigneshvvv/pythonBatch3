from openpyxl import Workbook

worbook = Workbook()

sheet = worbook.active

sheet["A1"] = "Name"
sheet["B1"] = "Age"

sheet["A2"] = "vignesh"
sheet["B2"] = 24

worbook.save("employees.xlsx")