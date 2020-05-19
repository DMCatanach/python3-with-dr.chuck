fname = input("Please enter file name: ") 

try: 
	fhand = open(fname) 
except: 
	if fname == "na na boo boo" : 
		print (fname.upper(), "TO YOU - You have been punk'd!") 
		exit() 
	else: 
		print("Sorry, file could not be opened:", fname) 
		exit()

def find_conf_num(str): 
	colpos = str.find(':') 
	num = str[colpos+1:] 
	num = float(num) 
	return num

count = 0 
confidence = 0
for line in fhand: 
	if not line.startswith("X-DSPAM-Confidence:") : continue 
	#else do the processing thing, without using "sum" for variable name or the function of that name
	count += 1
	confidence += find_conf_num(line) 
	average = confidence / count


print("Average spam confidence: ", average)