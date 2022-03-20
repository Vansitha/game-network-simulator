# *****************************************************************
# FILE: createNetwork.py
# Author: Vansitha Induja Ratnayake
# PURPOSE: All functionality and operations related to the world
#          is handled by the BuildNetwork class.
# REFERENCE: Parts of this file contains code logic from Lecture 4
#            Linked Lists slides. Reference can be found in the
#            relevant code block
# COMMENTS: files which use the BuilNetwork class access graph operations
#           from the self.network attribute
# REQUIRES: HashTable.py, Graph.py, pickle module
# LAST MOD: 15/10/21
# *****************************************************************

from HashTable import DSAHashTable
from Graph import DSAGraph
import pickle


class BuildNetwork:

    def __init__(self):

        self.filename = None
        self.nodeCodeHashTable = None
        self.edgeCodeHashTable = None
        self.network = None
        self.startNode = None
        self.targetNode = None  # * Can be modified in the program

    def nodeParameterTweaks(self, key, newValue):
        '''Responsible for updating the parameters of the nodes. 
        Takes in the existing node code and the new value as 
        arguements
        '''

        self.nodeCodeHashTable.update(key, newValue)
        self.network.updateAllNodes(key, newValue)

    def edgeParameterTweaks(self, key, newValue):
        '''Responsible for udating the parameters of the edges.
        Takes in the existing edge code and the new value to be set as
        arguements
        '''

        self.edgeCodeHashTable.update(key, newValue)
        self.network.updateAllEdges(key, newValue)

    # * Reading a file methods
    def readFile(self, filename):
        '''Text file is parased to extract the necessary data to create the graph 
        (world). Generated hash tables are used to save the edge and node parametrs. 
        '''

        self.filename = filename
        self.__generateEmptyHashTable()
        self.network = DSAGraph()
        Noerror = True

        try:
            with open(self.filename) as file:

                for data in file:
                    line = data.split()  # * used split method since it is an exception in file handling

                    if len(line) != 0:
                        # * Gets the node codes and stores it in a hash table
                        if line[0].lower() == 'ncode':
                            self.nodeCodeHashTable.put(line[1], line[2])

                        # *Add vertex from the file and using the node codes from the hash table
                        if line[0].lower() == 'node':
                            vertexValue = self.nodeCodeHashTable.get(line[2])
                            self.network.addVertex(
                                line[1], line[2], vertexValue)

                        # * Gets the edge codes and stores it in a hashtable
                        if line[0].lower() == 'ecode':
                            self.edgeCodeHashTable.put(line[1], line[2])

                        # * Add edge from the file and using the edge codes from the hash table
                        if line[0].lower() == 'edge':
                            edgeWeight = self.edgeCodeHashTable.get(line[3])
                            self.network.addEdge(
                                line[1], line[2], line[3], edgeWeight)

                        # * Get start node into a variable
                        if line[0].lower() == 'start':
                            self.startNode = line[1]

                        # * Get target node into a variable
                        if line[0].lower() == 'target':
                            self.targetNode = line[1]

        except IOError as e:
            Noerror = False

        return Noerror

    def readSerializedFile(self, filename):
        ''' Reads a serialiszed file to create the graph (world).
        Logic for reading a serialized file was obtained from the Lecture 4: Linked List
        slides.
        Reference: Maxville, Vallerie. 2021. LECTURE4: LINKED LISTS. PDF. https://lms.curtin.edu.au/bbcswebdav/pid-9239449-dt-content-rid-56299307_1/xid-56299307_1
        '''

        self.filename = filename

        noError = True

        try:
            with open(filename, "rb") as dataFile:
                self.network = pickle.load(dataFile)
                self.nodeCodeHashTable = pickle.load(dataFile)
                self.edgeCodeHashTable = pickle.load(dataFile)
                self.startNode = pickle.load(dataFile)
                self.targetNode = pickle.load(dataFile)

        except IOError as e:
            print("Load Error: ", e)
            noError = False

        return noError

    # * Saving data methods
    def saveToSerialized(self, saveFilename):
        ''' Saves serialized objects to the supplied file. 
        Logic for saving to a serialized file was obtained from the Lecture 4: Linked List
        slides.
        Reference: Reference: Maxville, Vallerie. 2021. LECTURE4: LINKED LISTS. PDF. https://lms.curtin.edu.au/bbcswebdav/pid-9239449-dt-content-rid-56299307_1/xid-56299307_1
        '''

        noError = True

        try:
            with open(saveFilename, "wb") as dataFile:
                pickle.dump(self.network, dataFile)
                pickle.dump(self.nodeCodeHashTable, dataFile)
                pickle.dump(self.edgeCodeHashTable, dataFile)
                pickle.dump(self.startNode, dataFile)
                pickle.dump(self.targetNode, dataFile)

        except IOError as e:
            print("Load Error: ", e)
            noError = False

        return noError

    def saveWorld(self, saveFilename):
        '''Writes the the list of vertices, edges and the adjacent vertices to the 
        supplied filename and outputs a text file'''

        noError = True

        verticesList = self.network.getAllVertices()
        edgeList = self.network.getAllEdges()
        adjacentList = self.network.getAllAdjacentVertices()

        try:
            with open(saveFilename, "w") as file:

                for vertex in verticesList:
                    file.write(vertex)
                    file.write('\n')

                file.write('\n')

                for adjacnet in adjacentList:
                    file.write(adjacnet)
                    file.write('\n')

                file.write('\n')

                for edge in edgeList:
                    file.write(edge)
                    file.write('\n')

        except IOError as e:
            noError = False

        return noError

    def saveGraph(self, data, saveFilename):
        '''Writes the weighted adjacency matrix representation of the graph the
        to a text file'''

        vertices = self.network.vertices

        noError = True
        try:

            with open(saveFilename, "w") as file:
                for vertex in vertices:
                    file.write(f" {vertex.getLabel()}")

                file.write('\n')

                for item in data:
                    writedata = str(item)
                    file.write(f"{writedata}")
                    file.write('\n')

        except IOError as e:
            noError = False

        return noError

    def saveRoutes(self, saveData, saveFilename):
        '''Writes all the generated routes to a text file'''

        noError = True

        try:
            with open(f"{saveFilename}", 'w') as file:
                for data in saveData:
                    file.write(data)
                    file.write('\n\n')

        except IOError as e:
            noError = False

        return noError

    def generateGraphRoutes(self):
        '''Find all the routes for the supplied start and target vertices and returns
        the linked list with all the routes'''

        generatedRoutes = self.network.generateRoutes(
            self.startNode, self.targetNode)

        return generatedRoutes

    # * Display methods
    def displayNodeCodes(self):
        '''Displays the hash table with all the node codes'''

        self.nodeCodeHashTable.display('e')

    def displayEdgeCodes(self):
        self.edgeCodeHashTable.display('e')

    def displayNetwork(self):
        '''Represent the simulated world by displaying all the vertcies, adjacent vertices
        and edges'''

        print("============== All Vertices ==============")
        self.network.displayVertices()

        print("\n=========== Adjacent Vertices ============")
        self.network.displayAdjacentVertices()

        print("================ All Edges ===============")
        self.network.displayEdges()

    # * Private methods
    def __generateEmptyHashTable(self):
        '''Reads the supplied file before the world (graph) is created to get the size of the hash tables
        required to store the node and the edge codes
        '''

        nodeCodeCount = 0
        edgeCodeCount = 0

        try:
            with open(self.filename) as file:
                for data in file:
                    line = data.split()  # * used split method since it is an exception for file handling
                    if len(line) != 0:
                        if line[0].lower() == 'ncode':
                            nodeCodeCount += 1
                    if len(line) != 0:
                        if line[0].lower() == 'ecode':
                            edgeCodeCount += 1

                self.nodeCodeHashTable = DSAHashTable(nodeCodeCount)
                self.edgeCodeHashTable = DSAHashTable(edgeCodeCount)

        except FileNotFoundError as e:
            print(e)
