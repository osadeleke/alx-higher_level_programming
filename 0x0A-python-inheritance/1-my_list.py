#!/usr/bin/python3
"""prints lists inherited
"""


class MyList(list):
    """child class of list
    """
    def __init__(self):
        self.list = list.__init__(self)
    
    def print_sorted(self):
        print(self.list)
