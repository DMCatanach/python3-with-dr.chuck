total = 0 
count = 0
while True: 
	number = input('Please enter a number: ')
	if number == 'done': 
		break 
	try: 
		float(number)   
	except: 
		print("Sorry, not a number.")
		continue
	total = total + float(number)
	count = count + 1
print(total, count, (total/count)) 
