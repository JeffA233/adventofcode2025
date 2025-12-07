

if __name__ == "__main__":
    file = open("day4/day4inp.txt", "r")
    data = file.read().splitlines()

    roll_dict = {}
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char == '@':
                roll_dict[(i, j)] = 1
            else:
                roll_dict[(i, j)] = 0

    tot_rolls = 0
    # for i, line in enumerate(data):
        # for j, char in enumerate(line):
    while True:
        counter = 0
        for (i, j), char in roll_dict.items():
            if char != 1:
                continue
            nearby_rolls = 0
            for add_i, add_j in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                try:
                    if roll_dict[(add_i + i, add_j + j)] == 1:
                        nearby_rolls += 1
                except KeyError:
                    continue

            if nearby_rolls < 4:
                tot_rolls += 1
                counter += 1
                roll_dict[(i, j)] = 0
            
        if counter == 0:
            break
    
    print(' ')
    print(' ')
    print(tot_rolls)