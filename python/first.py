# print("Hello World")

# message = "Hello world"
# print(message)

# message = "Hello crash course"
# print(message)

# message = "karan deep"
# message1 = "Karan deep "
# message2 = "karandeep ".rstrip()+"89"

# print(message.title() + " " + message1.rstrip() + "23"+message2)


# print(2*2+3)

# #syntax to create a list
# myList = ["one" , "two", "Three"]

# #to add values in a list
# myList.append("four")
# print(myList)

# #functions to remove values in a list.
# del myList[0]

# myList.pop()
# myList.pop(0)
# myList.remove("two")


#sort the list using inbuilt function

# myList2 = ["Karandeep", "Bhardwaj", "This", "is", "so", "random"]

# myList2.sort()
# print(myList2)

# myList2.sort(reverse = True)

# print(myList2)

# cars =["maruti", "wagon r", "santro", "alto"]

# print(sorted(cars))

# for car in cars:
#     print(car.title())

# for value in range(1,6):
#     print(value, sep=' ', end='', flush=True)

# print(cars[-1])

# print("should be in the next line")

# randomList = list(range(2,11,2))

# for value in randomList:
#     print(value)

# evenNumbers = [value for value in range(1,11,2)]
# print(evenNumbers)

# for value in range(1,6):
#     for anotherValue in range(1,value+1):
#         print("*", end="")
#     print()

# for value in range(12,0,-1):
#     for anotherValue in range(value-1,-1,-1):
#         print(" ", end="")
#         for star in range(anotherValue):
#             print("*",end=" ")
#         print()
#     print()

#Program to create a pyramid

# temp = 1
# for line in range(12,1,-1):
#     for spaces in range(line,0,-1):
#         print(" ", end=" ")
#     for leftAstric in range(0,temp):
#         print("*", end=" ")
#     for rightLine in range(1,temp):
#         print("*", end =" ")
#     print()
#     temp = temp+1

# temp1 = 12
# for newLine in range(0,12):
#     for space in range(0,newLine+1):
#         print(" ", end=" ")
#     for item in range(temp1,1,-1):
#         print("*", end =" ")
#     for items in range(temp1,0,-1):
#         print("*", end=" ")
#     print()
#     temp1 = temp1-1


# list = ["one", "two", "three", "four"]

# print(list[:3])

# #copying list in python

# deepCopyOfList = list[:]

# shallowCopyOfList = list

# #difference can be seen when appending elements to list


# #Condtional statements

# if 1 < 2 or 1 <= 2 and "Five".lower() not in list :
#     print("This works")
# else :
#     print("this doesnt work")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

if requested_toppings in available_toppings:
    print("Pizza can be made")
else:
    print("Cannot be made")


randomList =[]

if randomList:
    print("This is empty")
else:
    print("this does not work")

#dictionary

alien = {'color':'green', 'points':5}
print(alien['color'])

