"""
Polymorphism: More than one form or Multiple forms
Polymorphism types:
1.Compile time ( method overloading ): Same class and methods but different parameters
2.Run time ( method overriding ): Different class and same methods but different parameters
"""

# method overloading
class A:
    def sum(self, a, b):
        return a + b

    def sum(self, a, b, c):
        return a + b + c
# provides error without giving default parameter
# obj1 = A()
# print(obj1.sum(1, 2))

class B:
    def sum(self, a, b):
        return a + b

    def sum(self, a, b, c=1):   # provided default parameter
        return a + b + c
obj2 = B()
print(obj2.sum(1, 2, 3))


# method overriding
class A:
    def display(self):
        print("A class")


class B(A):
    def display(self):
        print("B class")
        super().display()   # using super keyword we are avoiding ambiguity


obj = B()
obj.display()
