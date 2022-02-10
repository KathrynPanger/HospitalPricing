from fuzzywuzzy import fuzz

def getBestMatch(matchContenders: list, targetString: str):
    contenderScores = {}
    for item in matchContenders:
        if item not in contenderScores:
            contenderScores[item] = fuzz.ratio(item, targetString)
    best_match = max(contenderScores, key=contenderScores.get)
    return best_match

def getRepresentativeMatch(matchContenders: list):
    allScores = {}
    for word in matchContenders:
        if word not in allScores:
            contenderScore = 0
            otherWords = set(matchContenders)
            for comparisonWord in otherWords:
                score = fuzz.ratio(comparisonWord, word)
                contenderScore += score
            print(contenderScore)
            allScores[word] = contenderScore * matchContenders.count(word)
    rep_match = max(allScores, key=allScores.get)
    print(allScores)
    return rep_match

test = [
#    "CDM Master Sheet",
    "CDM",
    "CDM SHEET",
    "cdm_sheet",
    "cdm",
    "chargemaster data",
    "chargemaster",
#    "CM data",
    "CDM data",
    "CM",
    "The great book of Chargemaster Data"
]

test2 = [
    "surgery",
    "surgery",
    "Surgery",
    "Surgery",
    "Surgery",
    "Surgury",
    "surgery",
    "surgery",
    "Surgery",
    "surgerie",
    "ergery",
    "surgery",
]

print(getRepresentativeMatch(test))