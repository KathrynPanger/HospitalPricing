import pandas as pd
#workbook = pd.read_excel('../chargemaster-cdm-2021/AHMC Aanaheim Regional Medical Center/106301098_CDM_All_2021.xlsx')
#workbook.head()

import os
print(os.getcwd())
file = "../chargemaster-cdm-2021/Alvarado Hospital/106370652_CDM_All_2021.xlsx"
xls = pd.ExcelFile(file)
sheets = {}
for sheet_name in xls.sheet_names:
    sheets[sheet_name] = xls.parse(sheet_name)
    print(sheets)