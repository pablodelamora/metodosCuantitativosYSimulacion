def genSet(setNumber):
	if setNumber == 1:

		#(2^64)-1 = 18446744073709551615
		#Este numero es el maximo que se puede generar con 64 bits

		#return 4*3*(5**8),61,13
		return 4*3*(5**26),61,13 #este numero es 17881393432617187500
								 #representa el 96.9352280336% de el maximo de
								 #una computadora de 64 bits
	else:
		return 61*(5**8),306,13
		#return 61*(5**25),306,13 #este numero es 18,179,416,656,494,140,625
								 #representa el 98.5508151675% de el maximo de
								 #una computadora de 64 bits

def nextNumber(x0,m,a,c):
	return ((a*x0)+c) % m

def test(n,setNumber):
	m,a,c = genSet(setNumber)
	numbers = [1]
	for i in xrange(n):
		numbers.append(nextNumber(numbers[i],m,a,c))
	print 'len(numbers) = %d' % len(numbers)
	print 'len(set(numbers)) = %d' % len(set(numbers))

def quickTest():
	m,a,c = genSet(1)
	print float(m)/2**64
	m,a,c = genSet(2)
	print float(m)/2**64

if __name__=='__main__':
	#test(23828124,2)
	#test(1000000,2)
	#quickTest()
