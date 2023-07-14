# # While statements

# i = 1
# while i <= 5:
#   print(i)
#   i = i + 1 

# # If you 1_000, it makes the number more readable - its the same as 1000
# If you do print (i * '*') - while you can't concatinate strings and numbers, if you multiply - it will print it out, so so 5 * '*' is *****

#So far, we have done numbrers (which are numbers are floats), booleans, and strings -these are primitive data types
We have complex types as well, like lists
#Lists are used to represent a list of objects, like a list or names

names = ["Jamie", "Chris", "Opie"]
print(names[0]) will give you Jamie
you can also use negative index in Python
so print(names[-2]) gives you Chris
you can change objects at a given index
names[0] = "William" will update hte list
We can also select a range of values
so print(names[0:1])if you do a : it EXCLUDES THE NAME AT THE 1, THIS DOES motify the origianl list, it gives youa. new list

#List methods
Strings in Python are objects
lists are also objects so thye have methods too
numbers = [1, 2, 3, 4, 5]
numbers.append(6) adds an item to the end
numbers.insert(0, -1 ) first vale is hte index, second value is any type ofobject - this adds a -1 at the beginnign of list
numbers.remove(3) takes out the 3
numbers.clear() - removes all items in the list
print(1 in numbers) - checking to see if 1 is in numbers list, this is a boolean expression returning a boolean value - will give you true
print(len(numbers)) - number of elements in a list

#for loops
numbers = [1,2,3,4,5]
if yu want to print each item in a line, you use a for loop
for item in numbers: #this lets you iterate over each item in a list
  print(item)

you could do this with a while loop:
i = 0 
while i < len(numbers):
  print(numbers[i])
  i = i + 1

the range() Function
range function generates a sequence of numbers
range(5) -> this retruns a range object which can store a sequence of nubers
numbers = range(5) - EXCLUDES 5
you can also iterate over each number with a for loop
if you do range(5,10) -> starting and endign value, excluses end value
for number in numbers:
  print(number)

you can also add a third value which is a step 
numbers = range(5, 10, 2) - this would be 5, 7, 9
range functiosn are used as a part of for loops bc you don't need to store the result in a seperte variable
for number in range(5):

tuples 
tuples are like lists, we used them to store a sequence of bojects, but they are immuntable, we cant chagne htem once we create htem
numbers = [1,2,3] - this is a list
numbers = (1, 2, 3) - this is a tuple, see the paranthesis 
there are no built in methods really, just count and index - coutn is the number of occurances of an elment, index returns the index if the first occurance of hte given element 
the rest you see which have _add_ these are magic methods 
