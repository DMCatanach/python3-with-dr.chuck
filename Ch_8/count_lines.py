#read through mailbox data, print out second word on 'From' lines, and a count of how many such lines there were. 
#so a lot like the useful code from debugging.py, but with the added feature of adding to the count each time we have a 'From' line 

fhand = open('mbox-short.txt') 
count = 0 
for line in fhand: 
	words = line.split()
	if len(words) < 2 or words[0] != 'From:' : continue 
	print(words[1]) 
	count += 1 

print('There were {} lines in the file with From as the first word.'.format(count))