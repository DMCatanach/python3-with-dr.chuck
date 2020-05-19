#open words.txt
#make empty dictionary
#loop through to read each word 
#if word not already in dictionary, add it as a key 

fhand = open('words.txt') 
wordlist = dict() 
for line in fhand: 
	words = line.split()
	for word in words: 
		wordlist[word] = wordlist.get(word, 0) 
		
print(wordlist)