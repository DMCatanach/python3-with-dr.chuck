hrs = input('Enter Hours:')
rte = input('Enter Rate:')
hrs = float(hrs)  
rte = float(rte)
if hrs > 40: 
	pay = (40 * rte) + ((hrs - 40) * (rte * 1.5)) 
else: 
	pay = hrs * rte
print(pay)