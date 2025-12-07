if __name__ == '__main__':
    file = open('day2/day2inp.txt', 'r')
    data = file.read().splitlines()

    invalid_num = 0
    line = data[0]

    ranges = line.split(',')
    for id_range in ranges:
        range_nums = id_range.split('-')
        for i in range(int(range_nums[0]), int(range_nums[1]) + 1):
            # kinda cursed int to string to int conversion
            str_num = str(i)
            str_len = len(str_num)
            if str_len % 2 == 1:
                continue
            elif int(str_num[0:str_len // 2]) == int(str_num[(str_len // 2):str_len]):
                invalid_num += int(i)
            elif int(str_num[0]) == 0:
                invalid_num += int(i)

    print(invalid_num)