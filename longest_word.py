import re
def LongestWord(sen):
    # code goes here
    max_len = 0
    word = ''
    p = re.compile(r'[a-zA-Z0-9]+')
    for x in p.findall(sen):
        if len(x) >= max_len:
            max_len = len(x)
            word = x
    sen = word
    return sen


# keep this function call here
print(LongestWord('["one","three"]'))
