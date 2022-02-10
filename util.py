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

def pickFirstCDM(mixedCDMString):
    entry = mixedCDMString.split()
    for item in entry:
        try:
            int(item)
            return(item)
        except ValueError:
            continue


