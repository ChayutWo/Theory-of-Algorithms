"""
Math 590
Project 2
Fall 2019

p2stack.py

Partner 1: Chayut Wongkamthong
Partner 2:
Date: 10/30/2019
"""

"""
Stack Class
"""
class Stack:

    """
    Class attributes:
    stack    # The array for the stack.
    top      # The index of the top of the stack.
    numElems # The number of elements in the stack.
    """

    """
    __init__ function to initialize the Stack.
    Note: intially the size of the stack defaults to 100.
    Note: the stack is initally filled with None values.
    Note: since nothing is on the stack, top is -1.
    """
    def __init__(self, size=100):
        self.stack = [None for x in range(0,size)]
        self.top = -1
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        print(self.stack)
        print('Top: %d' % self.top)
        return ('numElems: %d' % self.numElems)

    """
    isFull function to check if the stack is full.
    input: -
    expected output: boolean True if the stack is full. False if it is not.
    """
    def isFull(self):
        ##### IMPLEMENT! #####
        # Check whether the number of elements in the stack is equal to the length
        return self.numElems == len(self.stack)

    """
    isEmpty function to check if the stack is empty.
    input: -
    expected output: boolean True if the stack is empty. False if it is not.
    """
    def isEmpty(self):
        ##### IMPLEMENT! #####
        # Check whether the number of elements in the stack is zero
        return self.numElems == 0

    """
    resize function to resize the stack by doubling its size.
    input: -
    expected output: -
    """
    def resize(self):
        ##### IMPLEMENT! #####
        # concatenate two list: the current stack and the empty stack with
        # the same size
        self.stack = self.stack + [None for i in range(len(self.stack))]
        return

    """
    push function to push a value onto the stack.
    input: val - a value to be push onto the stack
    expected output: -
    """
    def push(self, val):
        ##### IMPLEMENT! #####
        # Check whether the stack is full. If it is, resize it.
        if self.isFull():
            self.resize()

        # Add val onto the stack in the next index, update top and numElems
        self.top = self.top + 1
        self.stack[self.top] = val
        self.numElems = self.numElems +1
        return

    """
    pop function to pop the value off the top of the stack.
    input: -
    expected output: value stored in the stack at the top position
                     If called while the stack is empty, throw exception.
    """
    def pop(self):
        ##### IMPLEMENT! #####
        # Check whether the stack is empty, throw exception if it is.
        if self.isEmpty():
            raise Exception('The stack is currently empty.')
        else:
            # Else remove value from the top of the stack
            # Update top and numElems and return that value
            returnVal = self.stack[self.top]
            self.stack[self.top] = None
            self.top = self.top -1
            self.numElems = self.numElems - 1
        return returnVal
