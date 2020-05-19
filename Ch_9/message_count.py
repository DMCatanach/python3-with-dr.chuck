#like day_of_week.py, but with email address (index 1) instead of day

fname = input("Please enter a file name: ") 

try: 
	fhand = open(fname) 
except: 
	print("Sorry, could not open file called: ", fname) 
	exit()

email_addresses = {} 
for line in fhand: 
	words = line.split() 
	if len(words) < 2 or words[0] != 'From' : continue 
	email = words[1] 
	email_addresses[email] = email_addresses.get(email, 0) + 1	

print(email_addresses)