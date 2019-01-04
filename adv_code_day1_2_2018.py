def total_data():
    result = 0
    freq = [0]
    repeat = True
    while repeat:
        with open("input.txt", "r") as fo:
            data = fo.readlines()
            for d in data:
                if d is not None:
                    result += int(d.strip("\n"))
                    if result not in freq:
                        freq.append(result)
                    else:
                        repeat = False
                        return result

if __name__ == "__main__":
    print(total_data())