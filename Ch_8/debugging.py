#Excercises 2 & 3 of Python textbook, on p. 105

#The following program isn't fully guarded. Figure out how to make it fail, and then write a fix. (exercise 2)
#Also, rewriting guardian code to use one if statement (exercise 3)

fhand = open('mbox-short.txt') 
count = 0 
for line in fhand: 
	words = line.split()
	#print('Debug:', words)
	if len(words) < 3 or words[0] != 'From' : continue 
	print(words[2]) 

#This works, as in, it doesn't throw an error. But it also doesn't give us useful output, because all lines are skipped. 
#That's because all the lines that start with 'From:' have a length of 2. 
#So, we're asking for an index that doesn't exist in the lines we want. 
#To get useful output, we need to print index 1, because that's where the information we want is. 
#In that case, our guardian code could state < 2, and still work, without having to specify == 0. 
#That makes the code a little more flexible, because that way, we could make the desired output index a variable, 
#and len(words) < that variable + 1. 
#But!! It will work if we look for lines that start with 'From' instead of 'From:' Lines that start with 'From,' without the :, have more than two words.
	