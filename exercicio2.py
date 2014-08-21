def ehPrimo(num):
	if num <2:
		return 'false'
	elif num ==2:
		return 'true'
	else:
		for x in range(2,num):
			if num%x == 0:
				return 'false' 
				
	return 'true'

for y in range (101):
	print '%d '%(y)+ehPrimo(y)
	
