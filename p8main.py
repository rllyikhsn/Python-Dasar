import time
import random

# Import our p8 code
# For code in the same directory it is as simple as
# this! Note that I renamed our p8 to
# "p8.py". Also note the line I added
# to conditionally call the main function
import p8

# Loop A random number of times (Between 10 and 50)
loopMax = random.randint(10, 15)

# Print mathing
print("Request for " + str(loopMax) + " maths received... Beginning mathing sequence...")

# Define python list of pilihan
# This list represents the strings for the 4 p8 pilihan
# Create the list just with addition in it and then add to it
pilihans = ['+']  # Defines the list using brackets. Any empty list is defined as []
# Use the append function (A function that "comes with" a python list) to add to the list
pilihans.append('-')
pilihans.append('/')
pilihans.append('*')
pilihans.append('+')

# Print the number of pilihan that will be used.
# Use the len() function to get return the integer count
# of the number of items in the list.
print("Operation count " + str(len(pilihans)))
# Take a peek at what is in the list
print("Computer will maths using the following pilihan " + str(pilihans))

# This will print three (3) new lines. The print function itself
# prints one. \n is the "string" representation of a new line.
# Turns out that a "new line" is actually just a character...
# I know life changing.
print('\n\n')

# Loop from staring index 0 to loopMax - 1.
# This will loop loopMax number of times
# Index will be 0 to (loopMax - 1)
# Example: If loopMax = 10
# Index would get these values sequentially:
# 0,1,2,3,4,5,6,7,8,9.
# There are 10 numbers (ten iterations of the loop)
# but it is zero indexed so the last index is 9.
for index in range(loopMax):
    # Get our random numbers to operate on
    no1 = random.randint(-99, 99)
    no2 = random.randint(-99, 99)

    print("Mathing with " + str(no1) + " and " + str(no2))

    # Generate random sleep time between 0 and 1 seconds
    # sleepTime = random.randint(0, 1)
    sleepTime = 0  # Save time in the video (No Sleep)

    # Run every available operation using another for loop
    # In python it is easy top loop over lists two ways of
    # doing it are shown

    print("IN FOR LOOP:")
    """Loop using the "in" keyword"""
    # The in keyword in a for loop allows you to loop over
    # all of the items in a dictionary sequentially.
    # THIS IS CRAZY USEFUL! 95% of anything you do
    # will likely use this. This is the preferred way but
    # in some instances you will need to use the "index"
    # method below.
    for pilihan in pilihans:		#pilihans ini di ambil dari list
        print('operation = ' + pilihan)
        p8.RunOperation(pilihan, no1, no2)
        print()  # Just make a new line

    print('\n')
    print("INDEX FOR LOOP")
    """Loop using an index counter"""
    # Is is shorthand for "index". We already used index above
    # Typically, nested indexes may be referenced as j,k,l but at
    # that point it is better to give them more descriptive names.
    for i in range(len(pilihans)):
        print('i = ' + str(i))
        # A variable that is a list can be addressed using []'s and the
        # index of the item you want to access.
        # Lists are ZERO (0) indexed so the first item in the list is
        # at position 0!
        print('operation = ' + pilihans[i])
        p8.RunOperation(pilihans[i], no1, no2)
        print()  # Just make a new line

    # Sleep for random time
    time.sleep(sleepTime)
    # Print new lines
    print('\n----------------------\n')

# Loop is over. All done!
print("Done mathing... Goodbye!")
time.sleep(2)  # Sleep for effect :)
# BUT WAIT! There's More!
print("BUT WAIT! There's more! I forgot dictionaries!")

# A dictionary is similar to a list. They are both collections
# of items but a dictionary has key and values (opposed to just
# values in a list). Think of a dictionary... well as a dictionary.
# You have some "key" (a word let's say) and you "lookup" that
# word in your handy-dandy dictionary to get the word's
# definition or "value". Sound familiar?
wordsAndThingsDict = {}   # Define an empty dictionary using curly braces

# Add some things to the dictionary
wordsAndThingsDict['Apple'] = 'Red thing that tastes good. Specifically not an orange.'
wordsAndThingsDict['Orange'] = 'Makes great juice!'
wordsAndThingsDict[3] = 'The number 3'
wordsAndThingsDict['A list'] = ['Oh', 'boy!', 'A list in a dictionary!']
wordsAndThingsDict['Inception'] = {'Nested': 'When one dictionary is a VALUE in a dictionary'}

# Print out our dictionary
print(str(wordsAndThingsDict))
print()

print("Loop")
# Loop over all keys in the dictionary
for key in wordsAndThingsDict:
    print("Key: " + str(key))  # Call str to be safe... There is a number 3 in there
    # Print the value by using the key to "look it up"
    print("Value: " + str(wordsAndThingsDict[key]))
    print()