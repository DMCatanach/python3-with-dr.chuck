def computepay(hours, rate): 
	if hours > 40: 
		pay = (40 * rate) + ((hours - 40) * (rate * 1.5))
	else: 
		pay = hours * rate 
	return pay 

hrs = input('Enter Hours: ')
rte = input('Enter Rate: ')

try: 
	hrs = float(hrs)
	rte = float(rte) 
	total = computepay(hrs, rte) 
	print(total)
except: 
	print('Please use digits.')