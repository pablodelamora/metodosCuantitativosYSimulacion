def kolmogorov():
    numbers=[.54,.73,.98,.11,.68]
    #numbers=[.594, .928, .515, .055, .507, .351, .262, .797, .788,.442,.097,.798,.227,.127,.474,.825,.007,.182,.929,.852]
    #numbers=[.97,.11,.65,.26,.98,.03,.13,.89,.21,.69]
    numbers = sorted(numbers)

    numbersDPlus=[]
    numbersDMinus=[]

    for i in range(0,len(numbers)):
        #numbersDPlus.append(((i+1)/len(numbers))-numbers[i])
        #numbersDMinus.append(numbers[i]-(i/len(numbers)))
        aux1 = float(i+1)/float(len(numbers))
        aux2 = float(i)/float(len(numbers))

        numbersDPlus.append(aux1-numbers[i])
        numbersDMinus.append(numbers[i]-aux2)



    #print max(numbersDPlus)
    #print max(numbersDMinus)

    maxNumberDPlus = max(numbersDPlus)
    maxNumberDMinus = max(numbersDMinus)

    if maxNumberDPlus > maxNumberDMinus:
        maxNumber = maxNumberDPlus
    else:
        maxNumber = maxNumberDMinus

    print maxNumber


if __name__=='__main__':
    kolmogorov()
