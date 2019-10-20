"""
Math 590
Project 1: Sorting Algorithms
Fall 2019

Partner 1: Chayut Wongkamthong
Partner 2: NA
Date: 10/19/2019
"""

"""
SelectionSort
"""
def SelectionSort(listToSort):
    """
    Function Name: SelectionSort
    Objective: Perform sorting of the input array using Selection Sort algorithm
    Description: Loop through input array
                 Select the minimum of the unsorted portion
                 Correctly place it in the sorted portion
    Input: listToSort - A non-empty array of positive integer length.
                        The elements of the array must be comparable.
    Expected Output: A sorted array in an ascending order.
    """

    # Loop through the array and keep increasing the index to be sorted
    for sortedIndex in range(len(listToSort)):

        # Section array into sorted (index 0 to sortedIndex) and unsorted
        minElement = listToSort[sortedIndex]
        minIndex = sortedIndex

        # Find the minimum element (minElement) and its index (minIndex)
        # in the unsorted portion.
        for j in range(sortedIndex, len(listToSort)):
            if listToSort[j] < minElement:
                minElement = listToSort[j]
                minIndex = j

        # Swap that minimum element with the element at sortedIndex
        # This will make elements up to sortedIndex sorted in ascending order
        listToSort[sortedIndex], listToSort[minIndex] = minElement, listToSort[sortedIndex]
    return listToSort

"""
InsertionSort
"""
def InsertionSort(listToSort):
    """
    Function Name: InsertionSort
    Objective: Perform sorting of the input array using Insertion Sort algorithm
    Description: Loop through input array
                 Consider each element from left to right
                 Exchange it with elements to its left until it is in place
    Input: listToSort - A non-empty array of positive integer length.
                        The elements of the array must be comparable.
    Expected Output: A sorted array in an ascending order.
    """

    # Loop through the array and keep increasing the index to be sorted
    for sortedIndex in range(1,len(listToSort)):

        # Find the correct position of the element at sortedIndex
        # in the sorted portion.
        for i in range(sortedIndex, 0, -1):

            # If our new element is less than the previous element, swap them.
            if listToSort[i] < listToSort[i-1]:
                listToSort[i], listToSort[i-1] = listToSort[i-1], listToSort[i]
            # If not, it is in the correct position.
            else:
                break
    return listToSort

"""
BubbleSort
"""
def BubbleSort(listToSort):
    """
    Function Name: BubbleSort
    Objective: Perform sorting of the input array using Bubble Sort algorithm
    Description: Scan and swap any adjacent elements that are out of order
                 Repeat until no more pairs are swapped in the loop
    Input: listToSort - A non-empty array of positive integer length.
                        The elements of the array must be comparable.
    Expected Output: A sorted array in an ascending order.
    """

    # Set up counter (k) and boolean swap to check whether we perform
    # any swap in the loop or not
    k = 0
    swap = True

    # While there are some swaps made in the loop, repeat the checking process
    while swap:
        swap = False
        # Consider comparing pairs from index 0 to n-k
        for i in range(1, len(listToSort)-k):

            # If adjacent elements are in incorrect order, swap them and
            # mark that we swap in that round (swap = True)
            if listToSort[i] < listToSort[i-1]:
                listToSort[i], listToSort[i-1] = listToSort[i-1], listToSort[i]
                swap = True
        k = k + 1
    return listToSort

"""
MergeSort
"""
def MergeSort(listToSort):
    """
    Function Name: MergeSort
    Objective: Perform sorting of the input array using Merge Sort algorithm
    Description: Split array into halves
                 Recursively sort each half
                 Merge them back in the correct order
    Input: listToSort - A non-empty array of positive integer length.
                        The elements of the array must be comparable.
    Expected Output: A sorted array in an ascending order.
    """

    # If the array is singleton, it is already sorted
    if len(listToSort) < 2:
        return listToSort
    # If the array has 2 elements, swap them if necessary and return
    elif len(listToSort) == 2:
        if listToSort[0] <= listToSort[1]:
            return listToSort
        else:
            listToSort[1], listToSort[0] = listToSort[0], listToSort[1]
            return listToSort

    # Else, split them into halves and sort each of them using merge sort.
    else:
        half = len(listToSort)//2
        leftMerge = MergeSort(listToSort[:half])
        rightMerge = MergeSort(listToSort[half:])

        # After sorting each half, merge them back
        # Iterate through them simultaneously and compare the smallest element
        # in each half that isn't put into the output.
        # The smallest of the two will be put into the merged array (listToSort).
        leftIndex = 0 # track smallest element that isn't inserted from left array
        lenLeft = len(leftMerge)
        rightIndex = 0 # track smallest element that isn't inserted from right array
        lenRight = len(rightMerge)
        i = 0
        while leftIndex < lenLeft and rightIndex < lenRight:

            # If the left element is smaller, it will be inserted into output array
            if leftMerge[leftIndex] <= rightMerge[rightIndex]:
                listToSort[i] = leftMerge[leftIndex]
                leftIndex = leftIndex + 1
                i = i+1

            # Else, the right element will get inserted
            else:
                listToSort[i] = rightMerge[rightIndex]
                rightIndex = rightIndex + 1
                i = i+1

        # The elements that are left and not inserted into the output will be inserted
        if leftIndex == lenLeft:
            listToSort[i:] = rightMerge[rightIndex:]
        else:
            listToSort[i:] =  leftMerge[leftIndex:]
    return listToSort

"""
QuickSort

Sort a list with the call QuickSort(listToSort),
or additionally specify i and j.
"""
def QuickSort(listToSort, i=0, j=None):
    """
    Function Name: QuickSort
    Objective: Perform sorting of the input array from index i to j-1 inclusive
               using Selection Sort algorithm
    Description: Choose a pivot element (jth element in this implementation)
                 Partition the array. Put smaller items before the pivot and larger after
                 Recursively perform the first two step on each partition
    Input: listToSort - A non-empty array of positive integer length.
                        The elements of the array must be comparable.
           i - start index to be sorted (inclusive)
           j - end index to be sorted (exclusive)
    Expected Output: A sorted array in an ascending order in position i
                     up to but not include j.
    """

    # Set default value for j if None.
    if j == None:
        j = len(listToSort)

    # If the sorting range is 1, that partition is already sorted
    if i == j - 1:
        return listToSort

    # Else, use last element as the pivot
    else:
        pivot = listToSort[j-1]
        frontIndex = i

        # Loop through array from left to right
        for ind in range(i, j-1):

            # Move every element that is less than pivot to the left portion of the array
            # (using frontIndex to keep track of the position)
            if listToSort[ind] <= pivot:
                listToSort[ind], listToSort[frontIndex] = listToSort[frontIndex], listToSort[ind]
                frontIndex = frontIndex + 1

        # Move pivot element to the correct position (next to the smaller element portion)
        listToSort[frontIndex], listToSort[j-1] = pivot, listToSort[frontIndex]

        # Recursively sort each partition. In this case, we actually implement the algorithm in place.
        # Check that there are some elements in left/right portion, and partition them recursively
        if frontIndex != i:
            temp1 = QuickSort(listToSort, i, frontIndex)
        if frontIndex != j-1:
            temp2 = QuickSort(listToSort, frontIndex+1, j)
    return listToSort

"""
Importing the testing code after function defs to ensure same references.
"""
from project1tests_updated import *

"""
Main function.
"""
if __name__ == "__main__":
    print('Testing Selection Sort')
    print()
    testingSuite(SelectionSort)
    print()
    print('Testing Insertion Sort')
    print()
    testingSuite(InsertionSort)
    print()
    print('Testing Bubble Sort')
    print()
    testingSuite(BubbleSort)
    print()
    print('Testing Merge Sort')
    print()
    testingSuite(MergeSort)
    print()
    print('Testing Quick Sort')
    print()
    testingSuite(QuickSort)
    print()
    print('DEFAULT measureTime')
    print()
    measureTime()
