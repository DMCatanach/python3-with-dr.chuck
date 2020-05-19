#like message_count.py, but tracks domains instead of full addresses 
#so, there will be some slicing involved before putting things in the dictionary 

fname = input ("Please enter a file name: ") 

try: 
	fhand = open(fname) 
except: 
	print("Sorry, could not open the file called: ", fname) 

domains = {} 
for line in fhand: 
	words = line.split() 
	if len(words) < 2 or words[0] != 'From' : continue 
	email = words[1]
	#split on the @ to get the domain
	domain = email.split('@')[1]
	domains[domain] = domains.get(domain, 0) + 1

print(domains)