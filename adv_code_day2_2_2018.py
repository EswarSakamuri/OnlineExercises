def get_str():
    match = ['','',30]
    with open("input.txt", "r") as fo:
        data = fo.readlines()
        for i in range(0,len(data)-1):
            differ = 0
            if len(data[i].strip("\n")) == len(data[i].strip("\n")):
                for j in range(0,len(data[i].strip("\n"))):
                    if data[i].strip("\n")[j] != data[i+1].strip("\n")[j] :
                        differ += 1
                    else:
                        continue
                if differ < match[2]:
                    match  = [str(data[i].strip("\n")), str(data[i+1].strip("\n")), differ]
    print(match)


if __name__ == "__main__":
    get_str()