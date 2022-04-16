#https://www.cms.gov/medicaremedicare-fee-service-paymentphysicianfeeschedpfs-relative-value-files/rvu21d

from hospital import Hospital
from util import getBestMatch
import os

# folder = "../chargemaster-cdm-2021/Alameda Hospital"
# testHospital = Hospital(folder)
# docs = testHospital.documents
# one_doc = docs['106010735_CDM_All_2021.xlsx']
# sheets = (one_doc.sheets)
# ab1045 = sheets["AB 1045"]
# data = ab1045.data
# print(data)


directory = "../chargemaster-cdm-2021/"
subfolders = [ f.path for f in os.scandir(directory) if f.is_dir() ]


#Rename all AB 1045 forms to be called "AB1045"
for folder in subfolders[0:10]:
    hospital = Hospital(folder)
    documents = hospital.documents
    for key, value in documents.items():
        match = getBestMatch([name for name in value.sheetNames],
                             "AB 1045", 38)
        if match is not None:
                AB1045 = value.sheets[match]
                AB1045.name = "AB1045"

#print(forms)

for folder in subfolders[0:10]:
    hospital = Hospital(folder)
    documents = hospital.documents
    forms = []
    for key, value in documents.items():
        match1 = getBestMatch([name for name in value.sheetNames],
                             "chargemaster", 38)
        match2 = getBestMatch([name for name in value.sheetNames],
                              "CDM", 38)
        if match is not None and match2 is not None:
                CDM = value.sheets[match]
                forms.append(CDM)
                #AB1045.name = "AB1045"

print(forms)