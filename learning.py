if 5 > 2:
  print("Five is greater than two!")


if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 


x = 5
y = "John"
print(x)
print(y)


x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


x = 5
y = "John"
print(type(x))
print(type(y))


a = 4
A = "Sally"
#A will not overwrite a


#legal variable names:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "awesome"
print("Python is " + x)


def myfunc():
  print("Python is " + x)

myfunc()

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

def myfunc():
  global x    #this makes the variable global
  x = "fantastic"

myfunc()

print("Python is " + x)


x = ["apple", "banana", "cherry"]

#display x:
print(x)

#display the data type of x:
print(type(x)) 


x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))














import random

print(random.randrange(1, 10))












a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


a = "Hello, World!"
print(a[1])   #this will print 2st caracter of a
              # this is because 1st caracter in python is fiven by 0


print("\n")

for x in "banana":
  print(x)



txt = "The best things in life are free!"
print("free" in txt)



txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")



txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
