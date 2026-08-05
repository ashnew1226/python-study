# class Animal:
#     def sound(self):
#         print("animal sound")
# class Dog(Animal):
#     def sound(self):
#         print("bark")
# d = Dog() # it will just create a d object for Dog class
# d.sound()

# Multiple Inheritance
# class Father:
#     def money(self):
#         print("money")
# class Mother:
#     def love(self):
#         print("love")
# class Child(Father,Mother):
#     pass

# c = Child()
# c.money()
# c.love()

# Multilevel Inheritance

# class Animal:
#     def eat(self):
#         print("can eat")

# class Dog(Animal):
#     def bark(self):
#         print("barks")

# class Puppy(Dog):
#     def weep(self):
#         print("weep")

# p = Puppy()
# p.eat()
# p.bark()
# p.weep()


# Hierarchical Inheritance

# class Animal:
#     def eat(self):
#         print("eating")

# class Dog(Animal):
#     def bark(self):
#         print("bark")

# class Cat(Animal):
#     def meow(self):
#         print("meow")


# d = Dog()
# c = Cat()

# d.eat()
# c.eat()
        

class Calculator:

    def add(self, a, b, c):
        return a+b+c


calc = Calculator()

print(calc.add(10,20,20))
print(calc.add(10,20,30))