def checksum():
    with open("input.txt", "r") as fo:
        checksum_dict = {}
        data_set = fo.readlines()
        for data in data_set:
            temp = {}
            for d in ''.join(set(data.strip("\n"))):
                if data.strip("\n").count(d) > 1:
                    temp[d] = data.strip("\n").count(d)
            li_temp = []
            for t in temp.items():
                if t[1] not in li_temp:
                    if t[1] in checksum_dict.keys():
                        checksum_dict[t[1]] +=1
                    else:
                        checksum_dict[t[1]] = 1
                    li_temp.append(t[1])
        print(checksum_dict)

if __name__ == "__main__":
    checksum()