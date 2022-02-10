def getBestMatch(matchContenters: list, targetString: str):
    from fuzzywuzzy import fuzz
    #from fuzzywuzzy import process

    contenderScores = {}
    for item in matchContenters:
        if item not in contenderScores:
            contenderScores[item] = fuzz.ratio(item, targetString)
    max_key = max(contenderScores, key=contenderScores.get)
    return max_key

