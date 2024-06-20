#This program says hello and asks the name of the user.

print("Hello, world!")
print("What is your name?") #Ask for the user's name.

myName = input() #input() waits for the user to type some text on the keyboard and press "ENTER".

print("It is good to meet you, " + myName)

print("The length of your name is: ")
print(len(myName))

print("What is your age?") #Ask for the user's age.

myAge = input() #input() waits for the user to type some text on the keyboard and press "ENTER".

print("You will be " + str(int(myAge) + 1) + " in a year.") #The str() will convert or cast the 
                                                            #integer value of myAge to string. 
                                                            #Because we cannot concatenate numeric values with strings directly.