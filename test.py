from document import Document
from hospital import Hospital
folder = "..\chargemaster-cdm-2021\Alameda Hospital"
testHospital = Hospital(folder)
testFile = (testHospital.docNames[0])
testPath = folder + f"\{testFile}"
testDocument = Document(testPath)
print(testDocument.sheets["CDM 062021"].loc[2:])