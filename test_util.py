from util import getRepresentativeMatch
from util import getFirstNumber
from util import getBestMatch

def test_getBestMatch():
    targetString = "Surgery Services (CPT Codes 10021-69990)"
    testList = [
        "Surgery Services for Patients Listed Below",
        "Surgery type I",
        "Surgery left knee",
        "Carpal Tunnel Surgery",
        "Medicine Services  (CPT Codes 90281-99607)"
        "Radiology Services  (CPT Codes 70010-79999)"
        "All services for surgery"
        "Surgery Services (10022 - 69990)"

    ]
    assert getBestMatch(testList, targetString) == "Surgery Services (10022 - 69990)"

def test_getRepresentativeMatch():
    # Get the word that is most like all the other words,
    # but in lowercase
    testList = [
        "Surgery",
        "Sergeruy",
        "Surgery",
        "Surgery",
        "Surgery",
        "Surgery,",
        "sergery",
    ]
    assert getRepresentativeMatch(testList) == "surgery"

def test_getFirstNumber():
    testString1 = '1903-3918'
    testString2 = "19000 or 18001"
    assert getFirstNumber(testString1) == 1903
    assert getFirstNumber(testString2) == 19000