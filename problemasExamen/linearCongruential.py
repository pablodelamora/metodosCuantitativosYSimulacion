def genSet():
    m = input("Dame el modulo: ")
    a = input("Dame a: ")
    c = input ("Dame c: ")
    return m, a, c

def nextNumber(x0,m,a,c):
	return ((a*x0)+c) % m

def test():
    n = input("Cuantos datos quieres: ")
    x0 = input("Dame x0: ")
    m,a,c = genSet()
    numbers = [x0]
    for i in xrange(n):
	    numbers.append(nextNumber(numbers[i],m,a,c))
    #print 'len(numbers) = %d' % len(numbers)
    #print 'len(set(numbers)) = %d' % len(set(numbers))
    print  numbers

def completeCycle():
    x0 = input("Dame x0: ")
    m,a,c = genSet()
    numbers = [x0]
    i=0
    while i<m-1:
        numbers.append(nextNumber(numbers[i],m,a,c))
        i = i+1
        if len(numbers) != len(set(numbers)):
            print "No es un ciclo completo"
            break;

    if len(numbers) == len(set(numbers)):
        print "Si cumple el ciclo completo"
    #print numbers
    print len(numbers)
    print len(set(numbers))

if __name__=='__main__':
    #test()
    #completeCycle()
    print ("1. Escoger el numero de datos a imprimir (no incluye la semilla)")
    print ("2. Verificar si cumple el ciclo completo")
    op = input("Escoge una opcion: ")

    if (op == 1):
        test()
    if(op == 2):
        completeCycle()
