# String / sequence of characters/ either single or double quotes 
# Print is a function 
# print("Hello World")

#Variables temporarily store data in a computer's memory
#declare a variable by typing a name for variable, then equal sign, then value
#program gets executed top to bottom, so you can update variables
#python you can use decimal values for numbers
#pyton you should use underscore for multiword variables 
#can use a string as the value for a variable
#boolean true and false
#case sensitive language, so booleans need to be Truth or False
# age = 33
# age = 34
# price = 19.95
# first_name = "Jamie"
# is_online = False
# print(age)

#Receiving input from the user, make sure you have the space
# name = input("What is your name? ")
# print("Hello " + name) #this is string concatination

#Type Conversion
#There are three types of data in Python number, string, booleans - you can convert these types
#Whenever we call input function, it returns value as a string, even if we enter a number
# birth_year = input("Enter your birth year: ")
# age = 2023 - int(birth_year)
# print(age)

#float is for converting values to floating point number, floats are numbers with decimal - 10 is an integer, 10.1 is a float
# int()
# float()
# bool() #convert to boolean
# str() #convert to string

#Calculator exercise
# first_num = input("Enter the first number: ")
# second_num = input("Enter the second number: ")
# # sum = int(first_num) + int(second_num)
# # total = str(sum)
# # print("Sum: " + total)
# # sum = str(float(first_num) + float(second_num))
# print("Sum: " + sum)

first = float(input("First: "))
second = float(input("Second: "))
sum = first + second 
print("Sum: " + str(sum))