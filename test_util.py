from util import getRepresentativeMatch
from util import getFirstNumber


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