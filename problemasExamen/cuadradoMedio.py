def nextNumber(x0):
    x1 = x0 ** 2
    x1 = map(int, str(x1))
    #print x1Exp
    aux = 0
    while len(x1) > 4:
        if aux==0:
            x1.pop(len(x1)-1)
            aux = 1
        else:
            x1.pop(0)
            aux = 0
    x1=''.join(map(str, x1))
    x1 = int(x1)
    #print x1
    #print x1Exp
    return x1


def test():
    cond = 0
    i = 0
    x0 = 4380
    numbers = [x0]

    while cond == 0:
        numbers.append(nextNumber(numbers[i]))
        i = i + 1
        if len(numbers) != len(set(numbers)):
        #if i == 5:
            cond = 1

    print len(numbers)
    print numbers


if __name__=='__main__':
    test()
