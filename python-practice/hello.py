# This program prints "Hello world!" to the console and asks for user's name.

print ("Hello world!")
print ("What is your name?") # ask for user's name
myName = input()
print ("It is good to meet you, " + myName)
print ("The length of your name is:")
print (len(myName))
print ("What is your age?") # ask for user's age
myAge = input()
print ("You will be " + str(int(myAge) + 1) + " in a year.")
