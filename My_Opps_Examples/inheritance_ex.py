# Single Inheritance
class Parent:
    def func1(self):
        print("I am Parent class")


# Inheriting parent class with child class
class Child(Parent):
    def func2(self):
        print("I am Child class")


# make sure we are creating a object for child class

child_class_obj = Child()

child_class_obj.func1()
child_class_obj.func2()

print("##############################################################################################################")


# Multilevel Inheritance
class Parent:
    def func1(self):
        print("I am Parent class")


# Inheriting parent class with child class
class Child(Parent):
    def func2(self):
        print("I am Child class")


# Inheriting child & parent with grandchild
class GrandChild(Child):
    def func3(self):
        print("I am GrandChild class")


# make sure we are creating a object for grandchild class

grand_child_class_obj = GrandChild()

grand_child_class_obj.func1()
grand_child_class_obj.func2()
grand_child_class_obj.func3()

print("##############################################################################################################")


# Hierarchical Inheritance
class Parent:
    def func4(self):
        print("I am Parent class")


# Inheriting parent class with child1 class
class Child1(Parent):
    def func5(self):
        print("I am Child1 class")


# Inheriting parent class with child2 class
class Child2(Parent):
    def func6(self):
        print("I am Child2 class")


# make sure we are creating a object for child1 and child2 separate

h_child1_class_obj = Child1()
h_child2_class_obj = Child2()

h_child1_class_obj.func4()
h_child1_class_obj.func5()
h_child2_class_obj.func6()

print("##############################################################################################################")


# Multiple inheritance

class Father:
    def func1(self):
        print("Father class")


class Mother:
    def func2(self):
        print("Mother class")


class Children(Father, Mother):
    def func3(self):
        print("children class")


children_class = Children()

children_class.func1()
children_class.func2()
children_class.func3()

print("##############################################################################################################")


# Super keyword use

class A:
    def __init__(self):
        print("A class")


class B(A):
    def __init__(self):
        print("B class")
        super().__init__()


obj = B()
