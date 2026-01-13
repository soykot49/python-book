x='john'
y=5
print(x)

#check the type of variable
print(type(y))

#assign multiple values
x , y ,z = "Orange" , "Banana" , "Cherry"
print(x)
print(y)
print(z)

#one value to multiple varibles
x= y = z = "Mango"
print(x)
print(y)
print(z)

#unpack a collection
fruits = ["apple" , "banana" , "cherry"]
x , y , z = fruits
print(x)
print(y)    
print(z)

#global varibles
x = "awesome"

def myfunc():
    print("Python is " + x)
myfunc()

#Create a variable inside a function, with the same name as the global variable
x = "fantastic"
def myfunc():
    x = "awesome"
    print("Python is " + x)

myfunc()
print("Python is " + x)

#If you use the global keyword, the variable belongs to the global scope:
def myfunc ():
    global k
    k = "great"

myfunc()

print("Python is " + k)

#To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)



