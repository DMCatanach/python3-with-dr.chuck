fname = input("Please enter file name: ") 
fhand = open(fname) 

for line in fhand: 
	print(line.upper().strip())

