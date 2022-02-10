from util import getRepresentativeMatch


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