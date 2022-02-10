from fuzzywuzzy import fuzz
import re


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


def getFirstCDM(mixedCDMString):
    entry = re.findall(r"[\w']+", mixedCDMString)
    for item in entry:
        try:
            return int(item)
        except ValueError:
            continue


print(getFirstCDM("1893-2948"))

