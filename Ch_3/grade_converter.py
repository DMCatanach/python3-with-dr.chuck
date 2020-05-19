score = input("Please enter a score between 0.0 and 1.0: ")
try: 
	score = float(score) 
	if score > 1.0: 
		print("Sorry, that score is too big.")
	elif score >= 0.9: 
		print("A")
	elif score >= 0.8: 
		print("B")
	elif score >= 0.7: 
		print("C")
	elif score >= 0.6:
		print("D")
	else:
		print("F")
	
except: 
	print("Sorry, that was not a numerical value.")