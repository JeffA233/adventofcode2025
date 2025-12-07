

def sign(x):
    return (1, -1)[x < 0]

if __name__ == '__main__':
    print(sign(0))
    file = open('day1/day1inp.txt', 'r')
    data = file.read().splitlines()

    dial = 50
    zeros_tot = 0
    for i in data:
        num = int(i[1:])

        passes = (num - (num % 100)) // 100
        if passes > 0:
            test = 0
        # dial_sign = sign(dial)

        if i[0] == 'R':
            if (num % 100) + dial >= 100 and dial != 0:
                passes += 1
            dial += num
        else:
            if dial - (num % 100) <= 0 and dial != 0:
                passes += 1
            dial -= num
        dial %= 100
        zeros_tot += passes
        
    # print(dial)
    print(zeros_tot)