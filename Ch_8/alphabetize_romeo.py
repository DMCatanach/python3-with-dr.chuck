#open romeo.txt
#read line by line, split into a list of words 
#for each word, check to see if it is already in a list; if not, add it
#to finish, sort alphabetically and print 

fhand = open('romeo.txt')
word_list = []
for line in fhand: 
	words = line.split()
	for word in words: 
		if word not in word_list: word_list.append(word) 
word_list.sort()
print(word_list)