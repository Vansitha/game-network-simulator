# ***************************************************************************
# FILE: HashTable.py
# Author: Vansitha Induja Ratnayake
# PURPOSE: General purpose hash table to store a key value pair
# REFERENCE: - This file has been submitted previously for DSA COMP1002 Practical 7
#            (Hash Tables) submission.
#            Ratanayke, Vansitha Induja. COMP1002 Graphs Practical 7 Submission
#              Parts of this file contains pseudocode logic from
#              lecture 8: Hash Tables and logic from external web sources.
#              Referenced in the appropriate method doc strings
# COMMENTS: None
# REQUIRES: math and numpy modules
#           (Note: numpy is an extenal python library)
# LAST MOD: 16/10/21
# **************************************************************************

import math
import numpy as np


class DSAHashEntry:

    def __init__(self, inKey, inValue):
        self.key = inKey
        self.value = inValue
        self.state = 1

    def getKey(self):
        return self.key

    def getValue(self):
        return self.value

    def setValue(self, invalue):
        self.value = invalue

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state

    def __str__(self):
        return(f"{self.key} : {self.value}")


class DSAHashTable:

    def __init__(self, tableSize):
        self.actualSize = self._nextPrime(tableSize)
        self.hashArray = np.full(self.actualSize, DSAHashEntry(None, None))
        self.count = 0

    # * Public methods
    def put(self, inKey, inValue):
        """Inserts key: value if an empty slot is found
        else if already populated probes until it finds a new slot
        """
        if self.getLoadFactor() >= 70:
            self._resize("grow")
        try:
            if self._hasKey(inKey) == False:
                hashIndex = self._hashFunction(inKey)

                if(self.hashArray[hashIndex].getKey() == None):
                    hashIdx = self._hashFunction(inKey)
                    self.hashArray[hashIdx] = DSAHashEntry(inKey, inValue)
                    self.count += 1

                else:
                    orginalIndex = hashIndex
                    hashIndex = (hashIndex + 1) % len(self.hashArray)

                    while(self.hashArray[hashIndex].getKey() != None):
                        hashIndex += 1

                        if hashIndex == orginalIndex:
                            raise Exception

                    self.hashArray[hashIndex] = DSAHashEntry(
                        inKey, inValue)
                    self.count += 1

        except Exception:
            print(f"Cannot find new index to insert {inKey}!")

    def get(self, inKey):
        """Gets value of supplied key if it exists"""

        try:
            hashIdx = self._find(inKey)
            return self.hashArray[hashIdx].getValue()
        except Exception:
            print("Cannot find Index!")

    def remove(self, inKey):
        """Remove entry of supplied key if it exists in array"""

        if self.getLoadFactor() <= 40:
            self._resize("shrink")
        try:
            hashIndex = self._hashFunction(inKey)

            if(self.hashArray[hashIndex].getState() == 0):
                hashIdx = self._hashFunction(inKey)
                self.hashArray[hashIdx] = DSAHashEntry(None, None)
                self.hashArray[hashIdx].setState(1)
                self.count -= 1

            else:
                hashIndex = self._find(inKey)
                self.hashArray[hashIndex] = DSAHashEntry(None, None)
                self.count -= 1

        except Exception:
            print("Cannot find an key!")

    def update(self, inKey, newValue):
        '''Update the value of the supplied key if it exists'''

        try:
            hashIdx = self._find(inKey)
            self.hashArray[hashIdx].setValue(newValue)
        except Exception:
            print("Cannot find key!")

    def getLoadFactor(self):
        """Calculates proportion(in %) of table that is occupied by entries"""

        loadFactor = self.getCount()/len(self.hashArray)
        return int(loadFactor * 100)

    def getCount(self):
        return self.count

    def display(self, mode=None):
        """Outputs hash table in terminal
        Mode set to 'e' ---> display only entries
        Default mode none ----> display entire table
        """

        for i in range(len(self.hashArray)):
            if mode == "e":
                if self.hashArray[i].getKey() != None:
                    print(f"{self.hashArray[i]}")
            else:
                print(f"{self.hashArray[i]}")

    # * Private methods
    def _resize(self, mode):
        """Grows and shrinks hash table which tries maintain
        a load factor between 70% and 40%
        """
        if mode == "grow":

            size = self._nextPrime(self.actualSize * 2)

            # * get a copy of the old hash table to extract the data
            originalArray = self.hashArray.copy()
            newArray = np.full(size, DSAHashEntry(None, None))

            self.hashArray = newArray  # create new hash table
            self.count = 0  # reset count for new table

            # * for each entry in the old hash table extract it and insert in to the new table with new indexes
            for entry in originalArray:
                if entry.getKey() != None:
                    key = entry.getKey()
                    value = entry.getValue()
                    self.put(key, value)

        if mode == "shrink":

            size = self._nextPrime(int(self.actualSize))

            # * get a copy of the old hash table to extract the data
            originalArray = self.hashArray.copy()
            newArray = np.full(size, DSAHashEntry(None, None))

            self.hashArray = newArray  # * create new hash table
            self.count = 0  # * reset count for new table

            # * for each entry in the old hash table extract it and insert in to the new table with new indexes
            for entry in originalArray:
                if entry.getKey() != None:
                    key = entry.getKey()
                    value = entry.getValue()
                    self.put(key, value)

    def _find(self, inKey):
        """linear probing to find the next empty slot if a slot is already populated.
           "Maxville. Valerie. 2020. "LECTURE6: HASH TABLES" PDF. https: // lms.curtin.edu.au/bbcswebdav/pid-9239451-dt-content-rid-56299311_1/xid-56299311_1

        (hash * second_hash) mod table_size
        Finds the next free slot in the table for a given key
        Returns original key if it fails"""

        hashIdx = self._hashFunction(inKey)
        origIdx = hashIdx
        found = False
        giveUp = False

        while not found and not giveUp:
            if(self.hashArray[hashIdx].getState() == 0):
                giveUp = True

            elif(self.hashArray[hashIdx].getKey() == inKey):
                found = True

            else:
                hashIdx = ((hashIdx + 1) % len(self.hashArray))

                if(hashIdx == origIdx):
                    giveUp = True

        if (not found):
            raise Exception

        return hashIdx

    def _hashFunction(self, key):
        #! Reference if using
        '''Hash Function takes in a string and return a hash index. Logic for string hash function
        obtained from an external web source.
        Webiste: GeeksForGeeks 
        Reference: 7maestro. 2021. "String hashing using Polynomial rolling hash function". GeeksForGeeks. https://www.geeksforgeeks.org/string-hashing-using-polynomial-rolling-hash-function/ (Authors real name is not displayed in the article page)'''

        p = 31
        m = 1e9 + 9
        power_of_p = 1
        hash_val = 0
        tableSize = (len(self.hashArray))

        for i in range(len(key)):
            hash_val = (
                (hash_val + (ord(key[i]) - ord('a') + 1) * power_of_p) % m)

            power_of_p = (power_of_p * p) % m

        return int(hash_val % tableSize)

    def _nextPrime(self, startVal):
        """Finds the next prime number
        Maxville. Valerie. 2020. "LECTURE6: HASH TABLES" PDF. https: // lms.curtin.edu.au/bbcswebdav/pid-9239451-dt-content-rid-56299311_1/xid-56299311_1
        """

        primeVal = None

        if startVal % 2 == 0:
            primeVal = startVal - 1
        else:
            primeVal = startVal

        isPrime = False
        while(not isPrime):
            primeVal = primeVal + 2
            isPrime = True
            rootVal = math.sqrt(primeVal)
            ii = 3
            while ((ii <= rootVal) and (isPrime)):
                if primeVal % ii == 0:
                    isPrime = False
                else:
                    ii += 2

        return primeVal

    def _hasKey(self, inKey):
        """Returns a bolean if supplied key is found in table"""

        found = False

        for entry in self.hashArray:
            if entry.getKey() == inKey:
                found = True

        return found
