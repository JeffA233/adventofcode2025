

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
            #dbg
            # if i == 1010:
            #     dbg = True

            # if i < 100:
            #     if int(str_num[0]) == int(str_num[1]):
            #         invalid_num += i
            # elif i < 1000:
            #     if int(str_num[0]) == int(str_num[1]) and int(str_num[1]) == int(str_num[2]):
            #         invalid_num += i
            # else:
            #     for length in range(1, (str_len // 2) + 1):
            #         if str_num[0:length] == str_num[length:length*2]:
            #             invalid_num += i

            if str_len % 2 == 1:
                # max length must be divisible by three for odd lengths
                max_compare_length = str_len // 3
                invalid_found = False
                for check in range(1, max_compare_length + 1):
                    if str_len % check == 0:
                        for window_start in range(0, str_len, check):
                            if window_start == str_len - check:
                                invalid_num += i
                                invalid_found = True
                                break
                            if int(str_num[window_start:window_start + check]) != int(str_num[window_start + check:window_start + (check * 2)]):
                                break
                    if invalid_found:
                        break
            else:
                # max length must be divisible by two for even lengths
                max_compare_length = str_len // 2
                invalid_found = False
                for check in range(1, max_compare_length + 1):
                    if str_len % check == 0:
                        for window_start in range(0, str_len, check):
                            if window_start == str_len - check:
                                invalid_num += i
                                invalid_found = True
                                break
                            if int(str_num[window_start:window_start + check]) != int(str_num[window_start + check:window_start + (check * 2)]):
                                break
                    if invalid_found:
                        break


    print(invalid_num)