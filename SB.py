def isPrime(n):
	if n<2:
		return False
	for x in range(2,int(n**0.5)+1):
		if n%x == 0:
			return False
	return True

def genPrime(n):
	num=0
	count = 0
	while(num<=n):
		if(isPrime(num) == True):
			count+=1
			print(num)
		num+=1
	return count


