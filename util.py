from fuzzywuzzy import fuzz
from typing import Optional
import re


def getBestMatch(matchContenders: list, targetString: str,
                 threshold: Optional[int] = None):
    contenderScores = {}
    targetString = targetString.lower()
    for item in matchContenders:
        item = item.lower()
        if item not in contenderScores:
            contenderScores[item] = fuzz.ratio(item, targetString)
    if threshold is not None and max(contenderScores.values()) < threshold:
        return None
    else:
        best_match = max(contenderScores, key=contenderScores.get)
        return best_match


def getRepresentativeMatch(matchContenders):
    allScores = {}
    wordCounts = {}
    matchContenders = map(lambda x: x.lower, matchContenders)
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
    return rep_match.lower()


def getFirstNumber(mixedCDMString):
    entry = re.findall(r"[\w']+", mixedCDMString)
    for item in entry:
        try:
            return int(item)
        except ValueError:
            continue

#
# def getBestMatchingRow(df, labels: list[str]):
#     contenderScore = 0
#     for i in range len(df):
#         row = df.iloc[i]
