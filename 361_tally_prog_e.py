"""
Problem:
5 Friends (let's call them a, b, c, d and e) are playing a game and need to keep track of the scores. ' \
'Each time someone scores a point, the letter of his name is typed in lowercase. ' \
'If someone loses a point, the letter of his name is typed in uppercase.
Give the resulting score from highest to lowest.
"""


def tally(t_str):
    res = {}
    for t in t_str:
        if t.lower() not in res.keys() and t.islower():
            res[t.lower()] = 1
        elif t.lower() not in res.keys() and t.isupper():
            res[t.lower()] = -1
        elif t.lower() in res.keys() and t.islower():
            res[t.lower()] += 1
        elif t.lower() in res.keys() and t.isupper():
            res[t.lower()] += -1
        else:
            pass
    return res


if __name__ == "__main__":
    result = {}
    test_str = ["dbbaCEDbdAacCEAadcB", "EbAAdbBEaBaaBBdAccbeebaec"]
    for s in test_str:
        res = tally(s)
        result[s] = res
    print(result)