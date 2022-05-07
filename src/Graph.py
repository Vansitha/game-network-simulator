# ***********************************************************************************
# FILE: Graph.py
# Author: Vansitha Induja Ratnayake
# PURPOSE: To create a general purpose graph data structure
# REFERENCE: This file has been submitted previously for DSA COMP1002 Practical 6
#            (Graphs) submission.
#            Ratanayke, Vansitha Induja. COMP1002 Graphs Practical 6 Submission
#            File also contains logic from external web sources.
#            Referenced in the appropriate method doc string.
# COMMENTS: Modified and restructured classes from the pracital 6
#           submission to meet assignment requirements
# REQUIRES: LinkedList.py and numpy module (external python library)
# LAST MOD: 15/10/21
# ************************************************************************************

from LinkedList import DSALinkedList
import numpy as np


class DSAGraphVertex:

    def __init__(self, inLabel, displayLabel, inValue):
        self.label = inLabel
        self.displayLabel = displayLabel
        self.value = inValue
        self.visited = False

    # * Getters and setters for a given vertex
    def getLabel(self):
        return self.label

    def setLabel(self, inLabel):
        self.label = inLabel

    def getDisplayLabel(self):
        return self.displayLabel

    def setDisplayLabel(self, inDisplayLabel):
        self.displayLabel = inDisplayLabel

    def getValue(self):
        return self.value

    def setValue(self, inValue):
        self.value = inValue

    def setVisited(self):
        self.visited = True

    def getVisited(self):
        return self.visited

    def clearVisited(self):
        self.visited = False

    def __str__(self):
        return(f"|Label: {self.label} | Display Label:{self.displayLabel} | Value: {self.value} |")


class DSAGraphEdge:

    def __init__(self, fromVertex, toVertex, inLabel, inValue):
        self.fromVertex = fromVertex
        self.toVertex = toVertex
        self.label = inLabel  # user sees this label
        self.value = inValue  # weight of the edge

    # * Getters and setters for a given edge
    def getLabel(self):
        return self.label

    def setLabel(self, inLabel):
        self.label = inLabel

    def getFromVertex(self):
        return self.fromVertex

    def setFromVertex(self, fromVertex):
        self.fromVertex = fromVertex

    def getToVertex(self):
        return self.toVertex

    def setToVertex(self, toVertex):
        self.toVertex = toVertex

    def getValue(self):
        return self.value

    def setValue(self, inValue):
        self.value = inValue

    def __str__(self):
        return(f"|{self.fromVertex}|--|{self.label}|--|{self.toVertex}| Weight: {self.value}")


class DSAGraph:

    def __init__(self):

        self.vertices = DSALinkedList()
        self.edges = DSALinkedList()

    # * Graph operations
    def addVertex(self, label, displayLabel, value):
        ''' Creats a new vertex with the supplied arugments if the vertex does not
        exisit already in the graph
        '''

        if self.getVertex(label) not in self.vertices:
            newVertex = DSAGraphVertex(label, displayLabel, value)
            self.vertices.insertLast(newVertex)

        else:
            print(f"Vertex {label} already in graph")

    def addEdge(self, fromVertex, toVertex, inLabel, inValue):
        ''' Adds an edge between two existing vertices in the graph using the
        supplied arguments
        '''

        if (self.hasVertex(fromVertex) and self.hasVertex(toVertex)) == True:
            if fromVertex != toVertex:
                newEdge = DSAGraphEdge(fromVertex, toVertex, inLabel, inValue)
                self.edges.insertLast(newEdge)
            else:
                print(
                    f"Invalid Edge: vertex {fromVertex} to vertex {toVertex}")
        else:
            fromVertexInGraph = self.hasVertex(fromVertex)
            toVertexInGraph = self.hasVertex(toVertex)

            if fromVertexInGraph == False:
                print(f"Invalid Edge: vertex {fromVertex} not in graph!")
            if toVertexInGraph == False:
                print(f"Invalid Edge: vertex {toVertex} not in graph!")

    def deleteEdge(self, fromVertex, toVertex):
        '''Delte an edge between two vertices that already has an edge. Currently method is not
        functional
        '''

        if (self.hasVertex(fromVertex) and self.hasVertex(toVertex)) == True:
            if self.hasEdge(fromVertex, toVertex) == True:
                edge = self.getEdge(fromVertex, toVertex)
                #   TODO: Need to implement linked list remove any node feature to remove any edge
                # * Currently features of the linked list are limited to removeFirst() and removeLast()
                # * if remove feature is implemented -> self.edges.remove(edge) this will delete the edge from the edge list
                # * As a result, the implementation of the delete edge functionality has come to a halt at the final stage.
            else:
                print(
                    f"Invalid Edge: No edge between {fromVertex} and {toVertex}")

        else:
            fromVertexInGraph = self.hasVertex(fromVertex)
            toVertexInGraph = self.hasVertex(toVertex)

            if fromVertexInGraph == False:
                print(f"Invalid Edge: vertex {fromVertex} not in graph!")
            if toVertexInGraph == False:
                print(f"Invalid Edge: vertex {toVertex} not in graph!")

    def deleteVertex(self, label):
        '''Deltes a vertex that exisits in the graph. Currently the method is not functional'''

        if self.hasVertex(label) == True:
            vertex = self.getVertex(label)
            #   TODO: Need to implement linked list remove any node feature to remove any vertex
            # * Currently features of the linked list are limited to removeFirst() and removeLast()
            # * if remove feature is implemented -> self.vertices.remove(vertex) this will delete the vertex from the vertex list
            # * As a result, the implementation of the delete vertex functionality has come to a halt at the final stage.

        else:
            print(f"Invalid Vertex: vertex {label} does not exist")

    def updateVertex(self, currentLabel, newLabel=None, newDisplayLabel=None, newValue=None):
        ''' Updates an existing vertex in the graph with the new values and  labels. newLabel,
        newDisplayLabel and newValue are optional arguements. Which means that and indiviual item can
        be changed at a given instance.
        '''

        if self.hasVertex(currentLabel) == True:
            if newLabel != None:
                if self.hasVertex(newLabel) == False:
                    vertex = self.getVertex(currentLabel)
                    vertex.setLabel(newLabel)

                    if newDisplayLabel != None:
                        vertex.setDisplayLabel(newDisplayLabel)

                    if newValue != None:
                        vertex.setValue(newValue)
                else:
                    print(f"Invalid Vertex: vertex {newLabel} already exists")

        else:
            print(f"Invalid Vertex: vertex {currentLabel} does not exist")

    def updateEdge(self, fromVertex, toVertex, edgeLabel=None, newvalue=None):
        '''Updates an existing edge between two vertices with the new values. edgeLabel and 
        newvalue are optional parameters which means that and individual item can be changed at
        a given instance.'''

        if (self.hasVertex(fromVertex) and self.hasVertex(toVertex)) == True:
            if (self.hasEdge(fromVertex, toVertex)) == True:
                edge = self.getEdge(fromVertex, toVertex)

                if edgeLabel != None:
                    edge.setLabel(edgeLabel)
                if newvalue != None:
                    edge.setValue(newvalue)

            else:
                print(
                    f"Edge Invalid: edge between {fromVertex} and {toVertex} does not exist")
        else:
            fromVertexInGraph = self.hasVertex(fromVertex)
            toVertexInGraph = self.hasVertex(toVertex)

            if fromVertexInGraph == False:
                print(f"Invalid Edge: vertex {fromVertex} not in graph!")
            if toVertexInGraph == False:
                print(f"Invalid Edge: vertex {toVertex} not in graph!")

    def updateAllEdges(self, edgeLabel, newValue):
        ''' This method is required for changing the parameter values of all nodes at 
        the same time. (Use: Parameter tweaks)'''

        for edge in self.edges:
            if edge.getLabel() == edgeLabel:
                edge.setValue(newValue)

    def updateAllNodes(self, displayLabel, newValue):
        '''This method is required for chaning the parameter values of all edges at the same.
        (Use: Parameter tweaks)'''

        for vertex in self.vertices:
            if vertex.getDisplayLabel() == displayLabel:
                vertex.setValue(newValue)

    # * All getters and setters for graph class
    # * Getters and setter for vertices
    def hasVertex(self, label):

        hasVertex = False
        vertex = self.getVertex(label)
        if vertex != None:
            if vertex.getLabel() == label:
                hasVertex = True

        return hasVertex

    def getVertex(self, label):
        ''' Iterates over the vertices and returns the vertex with the corresponding label '''

        getVertex = None

        for vertex in self.vertices:
            if vertex != None:
                if vertex.getLabel() == label:
                    getVertex = vertex

        return getVertex

    def getVertexCount(self):
        '''Returns the total number of vertices in the number'''

        vertexCount = 0
        for vertex in self.vertices:
            vertexCount += 1

        return vertexCount

    # * Getters and setters for edges
    def hasEdge(self, fromVertex, toVertex):
        '''Checks whether two given vertices has an edge between them and returns a boolean'''

        hasEdge = False
        edge = self.getEdge(fromVertex, toVertex)
        if edge != None:
            hasEdge = True

        return hasEdge

    def getEdge(self, fromVertex, toVertex):
        '''Returns the edge of two given vertices if they exists else returns none'''

        getEdge = None
        for edge in self.edges:
            if edge.getFromVertex() == fromVertex and edge.getToVertex() == toVertex:
                getEdge = edge

        return getEdge

    def getEdgeCount(self):
        '''Get the total number of edges between vertices in the graph'''

        edgeCount = 0
        for edge in self.edges:
            edgeCount += 1

        return edgeCount

    def getAdjacentVertex(self, label):
        '''Returns all the adjacent vetices for a given vertex'''

        adjacentList = DSALinkedList()

        if self.getVertex(label) != None:
            for edge in self.edges:
                if edge.getFromVertex() == label:
                    adjacentList.insertLast(edge.getToVertex())

        return adjacentList

    def getAllEdges(self):
        '''Returns a list of all the edges in the graph'''

        edgeList = DSALinkedList()

        for edge in self.edges:
            edgeList.insertLast(str(edge))

        return edgeList

    def getAllVertices(self):
        '''Returns a list of all the vertices in the graph'''

        vertexList = DSALinkedList()

        for vertex in self.vertices:
            vertexList.insertLast(str(vertex))

        return vertexList

    def getAllAdjacentVertices(self):
        '''Returns a list of all the adjacent vertices in the graph'''

        verticeslist = DSALinkedList()
        displayVertices = DSALinkedList()

        for vertex in self.vertices:
            verticeslist.insertLast(vertex.getLabel())

        for vertex in verticeslist:
            list = self.getAdjacentVertex(vertex)

            adjacentVertices = ''
            for item in list:
                adjacentVertices += item + ' '

            display = (f"{vertex} -> {adjacentVertices}")
            displayVertices.insertLast(display)

        return displayVertices

    def generateGraphMatrix(self):
        '''Generates a weighted adjacency matrix from the edge data stored in the graph. 
        Returns a 2d array containing all the data'''

        vertexCount = self.getVertexCount()
        edgeCount = self.getEdgeCount()

        vertexList = np.empty(vertexCount, dtype=object)
        edgeWeightList = np.zeros((vertexCount, vertexCount), dtype=int)

        # * Get a list of all the vertices in the graph to loop through each and get the edge weight if it exists
        count = 0
        for vertex in self.vertices:
            vertexLabel = vertex.getLabel()
            vertexList[count] = vertexLabel
            count += 1

        # * Check for whether each pair of vertices has an edge if so puts the edge weight to the edgeWeightList array
        countRow = 0
        for vertex in self.vertices:
            vertexLabel = vertex.getLabel()
            countCol = 0
            for eachVertex in vertexList:
                if self.hasEdge(vertexLabel, eachVertex) == True:
                    edge = self.getEdge(vertexLabel, eachVertex)
                    edgeWeight = edge.getValue()
                    edgeWeightList[countRow][countCol] = edgeWeight

                countCol += 1

            countRow += 1

        return edgeWeightList

    # * Graph traversal and display methods

    def displayVertices(self):
        '''Outputs all the vertices in the graph'''

        try:
            verticesList = iter(self.vertices)
            vertex = next(verticesList)
            for vertex in self.vertices:
                print(f"{vertex}")

        except StopIteration:
            print("Iteration Error: Cannot display vertices")

    def displayEdges(self):
        '''Outputs all the edges in the graph'''

        try:
            edgeList = iter(self.edges)
            edge = next(edgeList)
            for edge in self.edges:
                print(edge)

        except StopIteration:
            print("Iteration Error: Cannot display edges")

    def displayAdjacentVertices(self):
        '''Outputs all the adjacent vertices in the graph'''

        displayVertices = self.getAllAdjacentVertices()

        for item in displayVertices:
            print(item)

    def displayGraph(self):
        '''Outputs the weighted adjacency matrix'''

        vertexCount = self.getVertexCount()
        vertexList = np.empty(vertexCount, dtype=object)

        edgeWeights = self.generateGraphMatrix()

        # * Get a list of vertices into an array
        count = 0
        for vertex in self.vertices:
            vertexList[count] = vertex.getLabel()
            count += 1

        for item in vertexList:
            print(f" {item}", end='')

        print()

        count = 0
        for item in edgeWeights:
            vertex = vertexList[count]
            print(f"{vertex}{item}")
            count += 1

    def depthFirstSearch(self, startVertex, targetVertex, path, routes):
        '''Finds all the paths from a given start to a target vertex.
        Logic and structure for the method was obtained from an external source. 
        Website name: GeeksForGeeks
        Reference: Gupta, Shivam. 2021. "Print all paths from a given source to a destination." GeeksForGeeks. https://www.geeksforgeeks.org/find-paths-given-source-destination/
        '''

        startVertex.setVisited()
        path.insertLast(startVertex)

        if startVertex.getLabel() == targetVertex.getLabel():
            foundPath = ''
            previousVertex = None
            for item in path:
                if item.getVisited() == True:
                    if item.getLabel() != previousVertex:
                        previousVertex = item.getLabel()
                        foundPath += "-> " + item.getLabel() + ""

            routes.insertLast(foundPath)

        else:
            # * get start vertex label
            vertexLabel = startVertex.getLabel()

            # * find the adjacent list to the start vertex label
            adjacentList = self.getAdjacentVertex(vertexLabel)

            # * loop through adjacent vertices
            for vertex in adjacentList:
                nextVertex = self.getVertex(vertex)

                if nextVertex.getVisited() == False:
                    self.depthFirstSearch(
                        nextVertex, targetVertex, path, routes)

        path.removeLast()
        startVertex.clearVisited()

    def generateRoutes(self, start, target):
        '''Wrapper method to initiate depthFirstSearch algorithm.
        Logic and structure for the method was obtained from an external source. 
        Website name: GeeksForGeeks
        Reference: Gupta, Shivam. 2021. "Print all paths from a given source to a destination." GeeksForGeeks. https://www.geeksforgeeks.org/find-paths-given-source-destination/
        '''

        path = DSALinkedList()
        routes = DSALinkedList()

        startVertex = self.getVertex(start)
        targetVertex = self.getVertex(target)

        self.depthFirstSearch(startVertex, targetVertex, path, routes)

        return routes
