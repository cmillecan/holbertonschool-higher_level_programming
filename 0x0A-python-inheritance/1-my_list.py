#!/usr/bin/python3
class MyList(list):
    """
    MyList inherits from list
    """

    def print_sorted(self):
        """
        Prints an ascending sorted list
        """
        print(sorted(self))
