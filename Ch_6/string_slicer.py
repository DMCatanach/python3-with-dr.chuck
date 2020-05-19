str = 'X-DSPAM-Confidence:0.8475' 

#use find and string slicing to extract the portion after the colon (the number)
#convert extracted string to a float

colpos = str.find(':') 
num = str[colpos+1:]
num = float(num) 
print(num)