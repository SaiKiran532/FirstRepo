"""
Encapsulation: Wrapping up data (or) Combining variables and methods is known as encapsulation
"""


class Encap:
    __a = 10  # private variable

    def __display(self):  # private method
        print("Display method")


obj = Encap()
obj.__display()

"""
Above calling provides : AttributeError: 'Encap' object has no attribute '__display'
because we cannot access the private methods out of the class here we can see encapsulation as example.
"""
