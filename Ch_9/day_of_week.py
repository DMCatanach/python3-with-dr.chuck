#get day of week in lines that start with 'From' (no colon!), i.e. 3rd word, index 2 
#store day in dictionary, keep a running count (increment each time it occurs) 
#let's use entering the file name instead of hard-coding the file this time 

fname = input("Please enter file name: ") 

try: 
	fhand = open(fname) 
except: 
	print("Sorry, could not open file called: ", fname)
	exit() 

day_tally = {} 
for line in fhand: 
	words = line.split()
	if len(words) < 2 or words[0] != 'From' : continue 
	day = words[2]
	#print(day)
	day_tally[day] = day_tally.get(day, 0) + 1

print(day_tally)