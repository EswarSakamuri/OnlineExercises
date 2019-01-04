def total_data():
    result = 0
    with open("input.txt", "r") as fo:
        data = fo.readlines()
        for d in data:
            if d is not None:
                result += int(d.strip("\n"))
    return result

if __name__ == "__main__":
    print(total_data())