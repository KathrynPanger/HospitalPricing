from document import Document
from hospital import Hospital
import os

folder = "../chargemaster-cdm-2021/Alameda Hospital"
testHospital = Hospital(folder)
docs = testHospital.documents
excel_object = docs['106010735_CDM_All_2021.xlsx']
