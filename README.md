# PROGRAM README

# Program Description
The program generates a simulation of a virtualized world from a file.
Various scenarios may be imported into the software to investigate diverse facets and aspects of the environment.

# Version Information
- Developed in Python 3.8.10 64-bit
- Numpy 1.20.3

# Python3 Standared Libraires Utilised
- sys
- os
- pickle
- math
- timeit

# File Descriptions
- gameofcatz.py: main program file. Connects all functionality together
- createNetwork.py: Building the world and handling world operations
- userInterface.py: Front end for program
- Graph.py: Implementation of a generic graph data strcuture
- UnitTestGraph.py: Tests for Graph.py
- HashTable.py: Implementation of a generic hash table data strcuture
- UnitTestHashTable.py: Tests for HashTable.py
- LinkedList.py: Implementation of a generic linked list data structure
- UnitTestLinkedList.py: Tests for linkedList.py
- gameofcatz.txt: Test data
- pacman.txt: Test data
- snakeandladders2.txt: Test data
- README

# Dependencies
- gameofcatz.py: sys, timeit, userInterface.py, createNetwork.py
- createNetwork.py: pickle, Graph.py, HashTable.py
- userInterface.py: sys, os
- Graph.py: numpy, LinkedList.py
- UnitTestGraph.py: Graph.py
- HashTable.py: math, numpy
- UnitTestHashTable.py: HashTable.py
- LinkedList.py: None
- UnitTestLinkedList.py: LinkedList.py

# How to run the program
- The program has 3 different modes to choose from where each mode activated with differnt command line argunemnts.

- Mode1: Running no command line argunments will display on how to use the program.
- eg: python3 gameofcatz.py
- To select an option in the interative mode type the character within the brackets 
- eg: (1). Loadfile -> type '1' to select the load file option

- Mode2: Running with "-i" flag a command line argunement will activate the interative testing enviornment
- eg: python3 gameofcatz.py -i

- Mode3: When run with "-s inputfile.txt outputfile.txt," the simulation mode is activated, and the routes for the supplied input file are generated and output to the filename specified.
eg: python3 gameofcatz.py -s inputfile.txt outputfile.txt

# Program Version 1.0