from fuzzywuzzy import fuzz
import re


def getBestMatch(matchContenders: list, targetString: str):
    contenderScores = {}
    for item in matchContenders:
        if item not in contenderScores:
            contenderScores[item] = fuzz.ratio(item, targetString)
    best_match = max(contenderScores, key=contenderScores.get)
    return best_match


def getRepresentativeMatch(matchContenders: list[str]) -> str:
    allScores = {}
    wordCounts = {}
    uniqueWords = frozenset(matchContenders)
    for word in matchContenders:
        wordCounts[word] = matchContenders.count(word)
    for word in matchContenders:
        if word not in allScores:
            contenderScore = 0
            otherWords = uniqueWords - {word}
            for comparisonWord in otherWords:
                score = fuzz.ratio(comparisonWord, word)
                contenderScore += score
            allScores[word] = contenderScore * wordCounts[word]
    rep_match = max(allScores, key=allScores.get)
    print(allScores)
    return rep_match.lower()


def getFirstNumber(mixedCDMString):
    entry = re.findall(r"[\w']+", mixedCDMString)
    for item in entry:
        try:
            return int(item)
        except ValueError:
            continue


print(getFirstNumber("1893-2948"))

