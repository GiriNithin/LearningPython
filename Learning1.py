# Tuples -
x = () # Empty Tuple
print(x)

# tuple creation another way
tuple1 = tuple()
print(tuple1)

# creating a tuple with number
tuple2 = 1,2,3,4,5
print(tuple2)

#printing the last 4th element from a tuple
print(tuple2[-4])

#check if an element exists in a tuple - Returns a bool value
print(2 in tuple2)

#converting list to tuples
list2 = [1,2,3,4,5]
tuple3 = tuple(list2)
print(tuple3)

#tuple slicing
print(tuple3[1:3])
print(tuple3[2:5:2]) #Increments by two

