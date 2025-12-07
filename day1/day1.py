

if __name__ == '__main__':
    file = open('day1/day1inp.txt', 'r')
    data = file.read().splitlines()

    dial = 50
    num = 0
    for i in data:
        if i[0] == 'R':
            dial += int(i[1:])
        else:
            dial -= int(i[1:])
        dial %= 100
        if dial == 0:
            num += 1
        
    # print(dial)
    print(num)