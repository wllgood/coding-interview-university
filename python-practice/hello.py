# This program prints "Hello world!" to the console and asks for user's name.

print ("Hello world!")
print ("What is your name?") # ask for user's name
myName = input() # input() function waits for user input; creates myName variable to store input

print ("It is good to meet you, " + myName) # call myName variable to print user's name
print ("The length of your name is:")
print (len(myName)) # len() function returns length of string; it evaluates to an integer
print ("What is your age?") # ask for user's age
myAge = input() # store user's age in myAge variable
print ("You will be " + str(int(myAge) + 1) + " in a year.")
