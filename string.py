a = "hello world"
print(a)

# get character position in a string as strings are arrays
b="Doctor Stone"
print(b[3])

# looping through a string
for x in "Orange":
    print(x)


# check length of a string
z = "Demon Slayer"
print(len(z))

# check if something present in astring
text = "welocome to python programming"
print("python" in text)


# check if soomething not prsent in a string
txt = 'welcome home'
print('mars' not in txt)


# slicing strings
name = "Naruto Uzumaki"
print(name[1:5])   #arut


#slice from the start point
name = "Dazai Osamu"
print(name[:5])   #Dazai

# slice to the end point
name = "Osaka Nihon"
print(name[6:])


#negative indexing
name = "World war 2"
print(name[-5:-2] )

# modiify string 
x = "hello, world"

print(x.upper())
print(x.lower())
print(x.strip())  # removes whitespace
print(x.replace("h","j"))
print(x.split(","))    #split into two parts


# using f string to define
name = 'John'
age = 20
print(f'My name is {name} and age is {age}')


# display the value in a 2 decimal place
price = 40
print(f'the price is {price:.2f} usd')


#string methods

item = 'war and peace'
print(item.capitalize())
print(item.casefold())
print(item.center(20))  #center the rest with chracters like this (-----war and peace-----)

