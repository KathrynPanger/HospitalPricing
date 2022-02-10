#https://www.cms.gov/medicaremedicare-fee-service-paymentphysicianfeeschedpfs-relative-value-files/rvu21d
from document import Document
from hospital import Hospital
import os

folder = "../chargemaster-cdm-2021/Alameda Hospital"
testHospital = Hospital(folder)
docs = testHospital.documents
one_doc = docs['106010735_CDM_All_2021.xlsx']
sheets = (one_doc.sheets)
ab1045 = sheets["AB 1045"]
data = ab1045.data