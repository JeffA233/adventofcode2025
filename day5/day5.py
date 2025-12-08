def range_parser(line):
    line = line.split("-")
    return int(line[0]), int(line[1])

if __name__ == "__main__":
    file = open("day5/day5inp.txt", "r")
    data = file.read().splitlines()

    empty_line = 0
    ranges = []
    for i, line in enumerate(data):
        if line == "":
            empty_line = i
            break

        low, high = range_parser(line)
        # for i, (range_low, range_high) in enumerate(ranges):
            # range_above = range_high <= high
            # range_below = range_low >= low
            # low_range_within = range_low <= low <= range_high
            # high_range_within = range_low <= high <= range_high 
            
            # if not range_above and not range_below:
            #     ranges.append((low, high))
            #     continue

            # if range_above and low_range_within:
            #     ranges[i] = (range_low, high)
            
            # if range_below and high_range_within:
            #     ranges[i] = (low, range_high)
            
        ranges.append((low, high))
        
    tot_ids = 0
    for line in data[i+1:]:
        id = int(line)
        for range_low, range_high in ranges:
            if range_low <= id <= range_high:
                tot_ids += 1
                break

    print(' ')
    print(' ')
    print(tot_ids)
