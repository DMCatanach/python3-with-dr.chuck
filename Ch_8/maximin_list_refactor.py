#refactor maximin to use a list and min() and max() functions

number_list = []
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
	number_list.append(num)
	maximum = max(number_list)
	minimum = min(number_list)
print("Maximum:", maximum) 
print("Minimum:", minimum)