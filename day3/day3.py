

if __name__ == "__main__":
    file = open("day3/day3inp.txt", "r")
    data = file.read().splitlines()

    tot = 0
    for line in data:
        start = int(line[0])
        end = int(line[1])
        for i, char in enumerate(line[1:]):
            # weird to modify it but it works
            i += 1
            line_len = len(line)
            if i == line_len:
                break
            num = int(char)

            if num > start and i < line_len - 1:
                start = num
                end = int(line[i + 1])
            elif num > end:
                end = num
            
        end_num = start * 10 + end
        tot += end_num
            
    print(tot)