#like number_tally.py, but puts out maximum and minimum numbers instead of the average 
#this is the one that's graded 

largest = None
smallest = None
while True: 
	number = input('Please enter a number: ')
	if number == 'done': 
		break 
	try: 
		float(number)   
	except: 
		print("Sorry, not a number.")
		continue
	num = float(number)
	if largest is None or num > largest : 
		largest = num 
	if smallest is None or num < smallest : 
		smallest = num
print("Maximum", largest, "Minimum", smallest)