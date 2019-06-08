#Strings
name = "Sreeni Jilla"
namesq = 'xyz'

print(type(name))
print(type(namesq))

#access string content
print(name[0])
print(name[2:8])

#modify string content
name[0] = 'A' #Being string is immutable object, you can not edit

name2 = name + ' Hyd'
name = name + 'xyz'
print(name)
name = name.upper()
name = "mr"
name = name.capitalize()
print(name)
name = 'Sreeni Jilla'
name = concatenate(name, '10') #Use only + symbol for concatenate

name = name.replace('Mr','Miss')
print(name)
name = 10
name = 'Mumbaii'
isinstance(name, str) #True
isinstance(name, int) #False

          
#In python, strings can be stored in Double Quotes/Single Quotes
nameDQ = "Sreeni DQ"
print(type(nameDQ))

nameSQ = 'Sreeni SQ'
print(type(nameSQ))

#Access string content
name = 'Sreeni DS'
print(name[0])

#slicing
print(name[0:5])

#Modify string content
name = name + 'xyz' #You can concatinate
print(name)

#Replace function
name = name.replace(name, name.upper())
print(name)

#instance: Check for instance comparision
isinstance(name, str) 
isinstance(name, int)



#Functions
def add1(a,b):
    return a+b

def add2(a,b,c):
   tmp = a+b
   return tmp+c

#Defaulut values
def add3(a,b,c=20,d=40):
    tmp = a+b+c
    return tmp+d

print(add1(10,20))
print(add3(10))

#Add3 has 4 params
print(add3(3,4))
print(add3(3,4,10))
          
