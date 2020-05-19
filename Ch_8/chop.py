#exercise is on p. 101 of the book
#function modifies a list, removing the first and last elements
def chop(list): 
	del list[0]
	del list[-1]

#function returns a new list containing all but the first and last elements
def middle(list):
	return list[1:-1]


fruits = ["apples", "peaches", "cherries", "strawberies", "mangoes"]
print(fruits) #original list
chopped_fruit = chop(fruits) #modifies list
print(chopped_fruit) #return value is None, but the list is now modified
middle_fruit = middle(fruits) #creates new list
print(middle_fruit) #returns the middle element of the list, because original list was modified, and we created the new list from it
print(fruits) #this list is modified, because chop did that
