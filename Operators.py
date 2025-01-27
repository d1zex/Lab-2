#Operators are used to perform operations on variables and values.
#In the example below, we use the + operator to add together two values:
print(10 + 5) 

x = 5
y = 2
print(x % y)


x = 2
y = 5
print(x ** y) #same as 2*2*2*2*2

x = 15
y = 2
print(x // y)
#the floor division // rounds the result down to the nearest whole number

#Assignment operators are used to assign values to variables:
x = 5
print(x)

x = 5
x += 3
print(x)

x = 5
x -= 3
print(x)


x = 5
x *= 3
print(x)

x = 5
x /= 3
print(x)

x = 5
x%=3
print(x)

x = 5
x//=3
print(x)

x = 5
x **= 3
print(x)

x = 5
x &= 3
print(x)

x = 5
x |= 3
print(x)

x = 5
x ^= 3
print(x)

x = 5
x >>= 3
print(x)

x = 5
x <<= 3
print(x)

print(x := 3)

#Python Comparison Operators
#Comparison operators are used to compare two values:
x = 5
y = 3
print(x == y)
# returns False because 5 is not equal to 3

x = 5
y = 3
print(x != y)
# returns True because 5 is not equal to 3

x = 5
y = 3
print(x > y)
# returns True because 5 is greater than 3

x = 5
y = 3
print(x < y)
# returns False because 5 is not less than 3

x = 5
y = 3
print(x >= y)
# returns True because five is greater, or equal, to 3

x = 5
y = 3
print(x <= y)
# returns False because 5 is neither less than or equal to 3



#Python Logical Operators
#Logical operators are used to combine conditional statements:

x = 5
print(x > 3 and x < 10)
# returns True because 5 is greater than 3 AND 5 is less than 10

x = 5
print(x > 3 or x < 4)
# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)

x = 5
print(not(x > 3 and x < 10))
# returns False because not is used to reverse the result


#Python Identity Operators
#Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
# returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y, even if they have the same content
print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z)
# returns False because z is the same object as x
print(x is not y)
# returns True because x is not the same object as y, even if they have the same content
print(x != y)
# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y


#Python Membership Operators
#Membership operators are used to test if a sequence is presented in an object:
x = ["apple", "banana"]
print("banana" in x)
# returns True because a sequence with the value "banana" is in the list

x = ["apple", "banana"]
print("pineapple" not in x)
# returns True because a sequence with the value "pineapple" is not in the list

