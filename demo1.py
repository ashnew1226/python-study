# a =int(input("enter first number"))
# b =int(input("enter second number"))
# c = a+b
# print("addition of a and b is :",c)

# car = {"brand": "Ford","model": "Mustang","year": 1964}
# print(dict.fromkeys(car))

# for x,y in car.items():
#     print(f"{x} - {y}")
# carcopy = car.copy()
# print(carcopy)

# dictionary in python 

# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }
# for x,y in myfamily.items():
#     print(x,y)

#     for obj in y:
#         print(f"{obj}'-'{y[obj]}")

# x = ('key1', 'key2', 'key3')
# y = 0
# print(type(x))
# thisdict = dict.fromkeys(x, y)

# print(thisdict)


# while loop 

# i = 1
# while i < 6:
#     print(i)
#     i += 1
# else:
#   print("i is no longer less than 6")


# range function

# for i in range (1,20):
#     print(i)

# for i in range (1,20,2):  range(start, end, step)
#     print(i)


# for x in range(6):
#   if x == 3: break
#   print(x)
# else:
#   print("Finally finished!")


# nested loops

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)

# def country(name="India"):
#     print(f"i am from {name}")

# country("pak")
# country("aus")
# country("sl")   #output i am from pak
                #       i am from aus
                #       i am from sl
# Passing list/dict as a argument to function

# def my_func(food):
#     print(f"food is - {food}")
#     if type(food)==dict:
#         for i in food:
#             print(food[i]) 
        
#     else:
#         for i in food:
#             print(f"outside dictionary - {food[i]}")
# fruits = {"color":"red" ,"name":"banana"}
# my_func(fruits)
# positinal arguments
# def my_function(name,age):
#    print(f"name - {name}")
#    print(f"age - {age}")

# my_function("ashish",20)
# my_function(20,"ashish")
# positional arguments 
# keyword arguments
# default agruments
# arbitary aguments (variable-length arguments *args and **kwargs) - types 1) keyword arguments ,2) non keyword agruments
# lamda function arguments -> Lambda function take any number of arguments but can only have one expression 
# square = lambda x: x ** 2
# print(square(5))

# addition = lambda a,b: a + b
# print(addition(4,5))


# Combine Positional-Only and Keyword-Only
# Any argument before the / , are positional-only, and any argument after the *, are keyword-only.

# def my_function(a, b, /, *, c, d):
#   print(a + b + c + d)

# my_function(1, 2, c = 7, d = 8)


# # Recursion : 
# def factorial(n):
#     if n == 0:  # Base case
#         print("inside n = 0 ")
#         print(n)
#         return 1
#     else:       # Recursive case
#         print(f"inside the else part n = {n} n-1: {n-1}")
#         return n * factorial(n - 1)

# print(factorial(5))

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# # print(fibonacci(6))
# for i in range(6+1):
#     print(fibonacci(i))

# fibo series shorter virsion
# a, b = 0, 1
# for _ in range(7):
#     print(a)
#     a, b = b, a + b
# a = 0
# b = 1
# for i in range(7):
#     print(a)
#     temp = a
#     a = b
#     b = temp + b

# decorators decorators let you add extra behaviour to function without changing the function code 
# a decorator is a function that takes another function as input and return a new function

# def changecase(func):
#     def ucase():
#         return func().upper()
#     return ucase

# @changecase
# def my_function():
#     return "demo string"

# @changecase
# def new_function():
#     return "another string"
# print(my_function())
# print(new_function())

# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner

# @changecase
# def myfunction():
#   return "Hello "

# print(myfunction())
# If we are using decorators then metadata of original function will be lost (__name__) return the name of the function
# print(myfunction.__name__)
# for preservnig the metadata we use 'functools.wraps'



# Range Function # Pattern programs  
# n = int(input("enter number of rows"))    # Without space in pattern 
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range((2*i+1)):
#         print("*",end="")
#     print()
# n = int(input("enter number of rows"))      # with space in pattern
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end="")     
#     for j in range((i+1)):
#         print("* ",end="")
#     print()
    

# n = int(input("enter number of rows"))      # with space in pattern opposite to above
# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(" ",end="")     
#     for j in range((i)):
#         print(" *",end="")
#     print()


# n = int(input("enter the number")) #cby adding two and without whitespance in between
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(2*i+1):
#         print("*",end="")
#     print()

# Array 
# Python does not have a built in support for array instead it uses lists
# is a speical variable which holds more than one value at a time
# names = ["ashish","ashwin","vishal",'sagar',"ashwin"]

# print("all names are -")
# names.pop("ashwin")
# for i in names:
#     print(i) 

# List extend function
# fruits = ["banana","apple","kivi"]
# cars = ["maruti","audi","thar"]

# fruits.extend(cars)
# print(f"fruits - {fruits}")
# print(f"cars - {cars}")

# OOP Object Oreinted Programming
# allows you to structure your code using objects and classes
# provides clear structure to programs
# Make code easier to maintain, reuse and debug 
# Helps keep your code DRY (Do Not repeat yourself)
# allows you to build reusable application with less code.

# class Myclass:
#     x = 5
#     print(5)

# all classe have a method called __init__(). which is always executed when the class is been initiated

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# p1 = Person("ashish",29)
# print(p1.name)
# print(p1.age)

# class Person:                       #with __str__()
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"{self.name}{self.age}"
# p1 = Person("ashish",29)
# print(type(p1))
# print(p1)

# class Person():    # it is not compulsary to have name as "self" it can be anything but it must ne the first parameter of the any method of the class
#     def __init__(demo,name,age):
#         demo.name = name
#         demo.age = age
#     def myfunc(abc):
#         print(f"my name is {abc.name} and age is {abc.age}")

# p1 = Person("ashish",29)
# p1.age = 40
# p1.myfunc()

# Inheritance
# inheritance allows us to define a class that inherits all the methods and properties from another class
# parent class (base class): the class which is being inherited from
# child class (derived class): the class that inherites from another class
# Create a class named Person, with firstname and lastname properties, and a printname method:

# class Person:
#     def __init__(self,firstname,lastname):
#         self.firstname = firstname
#         self.lastname = lastname

#     def printname(self):
#         print(f"name - {self.firstname} {self.lastname}")

# p1 = Person("ashish","dede")
# p1.printname()

# class Student(Person):
#     pass
# s1 = Student("rohit","shinde")
# s1.printname()


# using init method


# class Person:
#     def __init__(self,firstname,lastname):
#         self.firstname = firstname
#         self.lastname = lastname

#     def printname(self):
#         print(f"name - {self.firstname} {self.lastname}")

# p1 = Person("ashish","dede")
# p1.printname()

# class Student(Person):
#     def __init__(self, firstname, lastname):
#         Person.__init__(self,firstname, lastname)
# s1 = Student("rohit","shinde")
# s1.printname()

# the same above inheritance can be acieved using the super()

# class Person:
#     def __init__(self,firstname,lastname):
#         self.firstname = firstname
#         self.lastname = lastname

#     def printname(self):
#         print(f"name - {self.firstname} {self.lastname}")

# p1 = Person("ashish","dede")
# p1.printname()

# class Student(Person):
#     def __init__(self, firstname, lastname,year):
#         super().__init__(firstname, lastname)# when we use super dont need to add self parameter it will automaticaly inherit the method and properties from its parent
#         self.graduationyear = year 
# s1 = Student("rohit","shinde",2025)
# s1.printname()
# print(s1.graduationyear)

# add welcome method to derived class

# class Person:
#     def __init__(self,firstname,lastname):
#         self.firstname = firstname
#         self.lastname = lastname

#     def printname(self):
#         print(f"name - {self.firstname} {self.lastname}")

# p1 = Person("ashish","dede")
# p1.printname()

# class Student(Person):
#     def __init__(self, firstname, lastname,year):
#         super().__init__(firstname, lastname)# when we use super dont need to add self parameter it will automaticaly inherit the method and properties from its parent
#         self.graduationyear = year
#     def welcome(self):
#         print(f"welcome student {self.firstname} {self.lastname} to the class of {self.graduationyear}") 
# s1 = Student("rohit","shinde",2025)
# s1.printname()
# print(s1.graduationyear)
# s1.welcome()
# Iterator
# Iterator is an object that contains a countable number of values
# list,set,tuple ,dictionries all are iterable objects they are iterable container which which you can get an iterator from

# mytuple = ("ashish","vishal","rohit")
# myit = iter(mytuple)
# print(next(myit))
# print(next(myit))
# print(next(myit))

# string = "ash"
# itstr = iter(string)
# print(next(itstr))
# print(next(itstr))
# print(next(itstr))
# print(next(itstr)) #throws error StopIteration

# object/class as an iterator we have to implement __iter__() and __next__() methods

# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         if self.a <= 5:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration   #it is used to stop iteration from going on forever

# myclass = MyNumbers()
# myiter = iter(myclass)
# for i in myiter:
#     print(i)

# Polymorphism it refers to method/functions/operators with the same name that that can be executed on many objects and classes.
# Function Polymorphism
# a = "hello"
# len(a) 

# class polymorphism
# is often used in class methods where we can have multiple classes with same method name
# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print("Drive")

# class Boat:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print("Sail")

# class Plane:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print("Fly")
    
# car1 = Car("Ford", "Mustang")
# boat1 = Boat("Ibiza", "Touring 20")
# plane1 = Plane("Boeing", "747")

# for i in (car1,boat1,plane1):
#     i.move()

# Inheritance using polymorphism

# class Vehicle:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print("move")

# class Car(Vehicle):
#     pass

# class Boat(Vehicle):
#     def move(self):
#         print("Sail")

# class Plane(Vehicle):
#     def move(self):
#         print("fly")

# c1 = Car("Ford","Mastang")
# b1 = Boat("Ibiza", "Touring 20")
# p1 = Plane("Boeing", "747")

# for x in(c1,b1,p1):
#     print(f"brand - {x.brand}")
#     print(f"model - {x.model}")
#     x.move()
# Module in python : by using the import statement we can use functions,all type of variables like array,dictionary,objects
# mymodule is the another which is stored at same location
# import mymodule

# a = mymodule.person1["name"]
# print(a)
# Rename a module :->
# import mymodule as mx

# a = mx.person1["age"]
# print(a)
# import platform 

# a = dir(platform)    # dir() can used on any modules
# print(a)
# from mymodule import person1 # when use from then dont need to call like 'mymodule.person1["name"]'
# print(person1["name"])
# Date time
# import datetime

# a = datetime.datetime.now()

# print(a.strftime("%a"))
# print(a.strftime("%A"))
# print(a.strftime("%w"))
# print(a.strftime("%d"))
# print(a.strftime("%b"))
# print(a.strftime("%B"))
# print(a.strftime("%m"))
# print(a.strftime("%y"))
# print(a.strftime("%Y"))
# print(a.strftime("%H"))
# print(a.strftime("%I"))
# print(a.strftime("%p"))
# print(a.strftime("%M"))
# print(a.strftime("%S"))
# print(a.strftime("%f"))
# print(a.strftime("%z"))

# a = datetime.datetime(2025,10,15) # year,month,day

# Python math
# a = min(3,5,1)
# b = max(54,21,80)
# print(a)
# print(b)
# a = abs(-7.05)   # abs function returns the absolute (positive) value of a specific number
# print(a)

# a = pow(4,3)
# print(a)
# import math 
# a = math.sqrt(64)
# print(a)
# print(math.ceil(1.6))
# print(math.floor(1.6))

# print(math.pi) # 3.141592653589793

# JSON in Python
# import json
# a = '{"name":"ashish","age":"19","designation":"developer"}'
# print(type(a))
# b = json.loads(a) # to convert string to json
# print(b)
# print(type(b))

# a = {"name":"ashish","age":"19","designation":"developer"}
# print(type(a))
# b = json.dumps(a) # to convert json to string 
# print(b)
# print(type(b))

# a = 40
# print(json.dumps(None))

# import json
# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
# a = json.dumps(x, indent=4, separators=(". ", " = "))
# # print(type(a))
# # print(a)
# asrot = json.dumps(x, indent=4, sort_keys=True)
# print(asrot)

# Regex Module

import re

# txt = "search the train"
# x = re.search("^search.*train$",txt)
# print(x)

# functions in re module
# findall() # Returns a list containing all matches
# seach() # Returns a match object if there is match anywhere in string 
# split() # Returns a list where the string has been split at each match
#sub() Replaces one ar many matches with a string

# txt = "search the train"
# a = re.findall("[a-z]",txt)
# print(type(a))
# print(a)

# a = "that is 20 Theeethat rupees Thisth"
# b = re.findall("^that",a)
# b = re.findall("th.{3}i",a)
# b = re.findall(r"\bth",a)  # /b beginning or at the end of word
# b = re.findall(r"\Bth",a)  # /B where the specified character is present or not
# b = re.findall(r"\d",a)  # /d search and check if there is any digit 
# b = re.findall(r"\D",a)  # /d search and check if there is not a single digit 
# b = re.findall(r"\s",a)  # /d check if there is a white space character 
# b = re.findall(r"\S",a)  # /d check if there is not a white space character 
# b = re.findall(r"\w",a)  # /w Returns a match where the string contains any word characters 
# b = re.findall(r"\W",a)  # /W Returns a match where the string DOES NOT contain any word characters	 
# print(b)

# txt = "The rain in Spain"
# a = re.findall("ai",txt)
# print(a)  #if no matches found using 'findall' the empty [] returned
# x = re.search("ash", txt)
# print(x)   #if no matches found using 'search' the None returned

#  split() Returns a ist where the string has been split at each match
# txt = "The rain in Spain"
# a = re.split("\s",txt)
# print(a)

# sub() :- function replaces the matches with teh text of your choice

# txt = "this is train"
# x = re.sub("\s","9",txt)
# print(x)

# txt = "this is train"
# x = re.sub("\s","9",txt,2) #can control the count of replacement (observ at location of '2')
# print(x)
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())