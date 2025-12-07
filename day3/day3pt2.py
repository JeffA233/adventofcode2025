

if __name__ == "__main__":
    file = open("day3/day3inp.txt", "r")
    data = file.read().splitlines()

    tot = 0
    for line in data:
        num_list = [(int(char), idx) for idx, char in enumerate(line)]
        top_twelve = []
        num_store = (0, 0)
        num_list_len = len(num_list)
        # get max num
        for num in num_list:
            if num[0] > num_store[0] and num[1] <= num_list_len - 12:
                num_store = num
        top_twelve.append(num_store[0])
        
        # start at max num idx and find next largest
        # assume number is largest if idx is within num_list_len - (12 - len(top_twelve)) of end
        while len(top_twelve) < 12:
            max_num = (0, 0)
            for num in num_list[num_store[1] + 1:]:
                if num[0] > max_num[0]:
                    max_num = num
                    num_store = num

                if num[1] >= num_list_len - (12 - len(top_twelve)):
                    break

            top_twelve.append(max_num[0])

        num_str = ''.join([str(i) for i in top_twelve])
        tot += num

    print(tot)