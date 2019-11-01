"""
Math 590
Project 2
Fall 2019

p2queue.py

Partner 1: Chayut Wongkamthong
Partner 2:
Date: 10/30/2019
"""

"""
Queue Class
"""
class Queue:

    """
    Class attributes:
    queue    # The array for the queue.
    front    # The index of the front of the queue.
    rear     # The index ONE PAST the rear of the queue.
    numElems # The number of elements in the queue.
    """

    """
    __init__ function to initialize the Queue.
    Note: intially the size of the queue defaults to 100.
    Note: the queue is initally filled with None values.
    """
    def __init__(self, size=3):
        self.queue = [None for x in range(0,size)]
        self.front = 0
        self.rear = 0
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        print(self.queue)
        print('Front: %d' % self.front)
        print('Rear: %d' % self.rear)
        return ('numElems: %d' % self.numElems)

    """
    isFull function to check if the queue is full.
    input: -
    expected output: boolean True if the queue is full. False if it is not.
    """
    def isFull(self):
        ##### IMPLEMENT! #####
        # Check whether numElems is equal the length of the queue
        return self.numElems == len(self.queue)

    """
    isEmpty function to check if the queue is empty.
    input: -
    expected output: boolean True if the queue is empty. False if it is not.
    """
    def isEmpty(self):
        ##### IMPLEMENT! #####
        # Check whether numElems is equal to zero
        return self.numElems == 0

    """
    resize function to resize the queue by doubling its size.
    Note: we also reset the front to index 0.
    input: -
    output: -
    """
    def resize(self):
        ##### IMPLEMENT! #####
        # Check whether our queue is currently wrapped around
        # Extract elements from the queue
        currentLen = len(self.queue)

        if self.rear > self.front:
            # if not, the current elements are in front:rear position
            self.queue = self.queue[self.front:self.rear]
        else:
            # if it is wrapped around, the current elements are in front to the end
            # and also from the start to the rear position
            self.queue = self.queue[self.front:] + self.queue[:self.rear]

        # Resize the queue to make sure we have queue with double
        # in size (currentLen*2)
        self.queue = self.queue + [None for i in range(len(self.queue), currentLen*2)]

        # Update all queue attributes
        self.front = 0
        self.rear = self.numElems

        return

    """
    push function to push a value into the rear of the queue.
    input: val - value to be push into the rear of the queue
    expected output: -
    """
    def push(self, val):
        ##### IMPLEMENT! #####
        # If the queue is full, resize it.
        if self.isFull():
            self.resize()

        # Change the value at the rear to val and update rear value
        self.queue[self.rear] = val
        self.rear = self.rear + 1

        # If the rear is over the queue, wrap around to the front (index 0)
        if self.rear == len(self.queue):
            self.rear = 0

        # Update the number of elements
        self.numElems = self.numElems + 1
        return

    """
    pop function to pop the value from the front of the queue.
    input: -
    expected output: the value at the front position
                     if the queue is empty, throw exception
    """
    def pop(self):
        ##### IMPLEMENT! #####
        # If the queue is currently empty, raise exception
        if self.isEmpty():
            raise Exception('The queue is currently empty.')
        else:
            # Record output value and remove it from the front of the queue
            outputVal = self.queue[self.front]
            self.queue[self.front] = None

            # Update the front position and the number of elements of the queue
            self.front = self.front + 1
            self.numElems = self.numElems -1
            # If the index is over the length of the queue, wrap around

            if self.front == len(self.queue):
                self.front = 0
        return outputVal
