#like message_count.py, but also does a maximum loop to find the item in the dictionary with the most messages 

fname = input("Please enter a file name: ")

try: 
	fhand = open(fname)
except: 
	print("Sorry, could not open the file called: ", fname)
	exit() 

email_addresses = {}
for line in fhand: 
	words = line.split() 
	if len(words) < 2 or words[0] != 'From' : continue 
	email = words[1]
	email_addresses[email] = email_addresses.get(email, 0) + 1

# print(email_addresses)

#then maximum loop to get the one with the biggest count 
largest = None
for email, count in email_addresses.items(): 
	if largest is None or count > largest: 
		largest = count 
		most = email
print(most, largest)

