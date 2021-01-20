programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}
print(programming_dictionary)

# retriveving items from dictionary
print(programming_dictionary["Bug"])

# adding newitems to dictionary

programming_dictionary["loop"] = "for loop and while loop"
print(programming_dictionary )

# empty dictionary 
empty_dict = {}

# wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

# edit an item in a dictionary
programming_dictionary["Bug"] = "a month in your computer"
print(programming_dictionary)

# loop through a dictionary
for key in programming_dictionary:
	print(key) # this line is gone print only key
	print(programming_dictionary[key]) # and this gona print values