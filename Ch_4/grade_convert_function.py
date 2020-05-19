def computegrade(score): 
	if score > 1.0: 
		return "Sorry, that score is too big."
	elif score >= 0.9: 
		return "A"
	elif score >= 0.8: 
		return "B"
	elif score >= 0.7: 
		return "C"
	elif score >= 0.6:
		return "D"
	else:
		return "F"

score = input("Please enter a score between 0.0 and 1.0: ")
try: 
	score = float(score)
	grade = computegrade(score) 
	print(grade)
except: 
	print("Sorry, that was not a numerical value.")