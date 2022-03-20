# ********************************************************************************************************
# FILE: LinkedList.py
# Author: Vansitha Induja Ratnayake
# PURPOSE: Implementation of a general purpose double ended linked list to store any type of data
# REFERENCE: This file has been submitted previously for DSA COMP1002 Practical 4
#            (Linked Lists) submission.
#            Ratanayke, Vansitha Induja. COMP1002 Graphs Practical 4 Submission
#            Implemented pseudocode from the lecture slides for DSAListNode class,
#            DSALinkedList class and the iterator methods.
#            Maxville. Valerie. 2020. "LECTURE4: LINKED LISTS" PDF. https://lms.curtin.edu.au/bbcswebdav/pid-9239449-dt-content-rid-56299307_1/xid-56299307_1
# COMMENTS: Modified implementation of a singly linked list fom the lecture slides to a doubly linked list
# REQUIRES: None
# LAST MOD: 16/10/21
# *********************************************************************************************************

class DSAListNode:

    def __init__(self, inVlaue):
        self.value = inVlaue
        self.next = None
        self.previous = None

    def getValue(self):
        return self.value

    def setValue(self, inValue):
        self.value = inValue

    def getNext(self):
        return self.next

    def setNext(self, newNext):
        self.next = newNext

    def getPrevious(self):
        return self.previous

    def setPrevious(self, previous):
        self.previous = previous


class DSALinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insertFirst(self, newValue):
        '''Inserts item from the head of the linked list'''

        newNd = DSAListNode(newValue)

        if self.isEmpty():
            self.head = newNd
            self.tail = newNd
        else:
            newNd.setNext(self.head)
            self.head.setPrevious(newNd)
            self.head = newNd

    def insertLast(self, newValue):
        '''Inserts item from the tail end of the linked list'''

        newNd = DSAListNode(newValue)

        if self.isEmpty():
            self.head = newNd
            self.tail = newNd
        else:
            self.tail.setNext(newNd)
            newNd.setPrevious(self.tail)
            self.tail = newNd
            self.tail.setNext(None)

    def isEmpty(self):
        '''Checks if the linked list is empty and returns a boolean'''

        empty = (self.head == None)

        return empty

    def peekFirst(self):
        '''Returns the data at the head node'''

        nodeValue = None

        if self.isEmpty():
            nodeValue
        else:
            nodeValue = self.head.getValue()

        return nodeValue

    def peekLast(self):
        '''Returns the data at the tail node'''

        nodeValue = None

        if self.isEmpty():
            nodeValue
        else:

            currNd = self.head
            while currNd.getNext() != None:
                currNd = currNd.getNext()

            nodeValue = currNd.getValue()

        return nodeValue

    def removeFirst(self):
        '''Remove an item from the head node'''

        nodeValue = None

        if self.isEmpty():
            nodeValue

        elif self.head.getNext() == None:
            nodeValue = self.head.getValue()
            self.head = None
            self.tail = None

        else:
            nodeValue = self.head.getValue()
            self.head = self.head.getNext()

        return nodeValue

    def removeLast(self):
        '''Remove an item fro the tail node'''

        nodeValue = None

        if self.isEmpty():
            nodeValue
        elif self.head.getNext() == None:
            nodeValue = self.head.getValue()
            self.head = None

        else:
            prevNd = None
            currNd = self.head

            while currNd.getNext() != None:
                prevNd = currNd
                currNd = currNd.getNext()

            nodeValue = currNd.getValue()
            self.tail = prevNd
            currNd = None

        return nodeValue

    def __iter__(self):
        '''Iterator method to to get next element in the list'''

        self.currNd = self.head
        return self

    def __next__(self):
        '''Next method to traverse through the list'''

        currValue = None

        if self.currNd == None:
            raise StopIteration
        else:
            currValue = self.currNd.getValue()
            self.currNd = self.currNd.getNext()

        return currValue
