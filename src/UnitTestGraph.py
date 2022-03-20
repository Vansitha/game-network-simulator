# ************************************************************************
# FILE: UnitTestGraph.py
# Author: Vansitha Induja Ratnayake
# PURPOSE: Test graph classs
# REFERENCE: None
# COMMENTS: Created a new test harness to test the modified graph class
# REQUIRES: DSAGraph from Graph.py
# LAST MOD: 14/10/21
# ************************************************************************

from Graph import DSAGraph


class TestGraph:

    def __init__(self):

        self.testGraph = DSAGraph()

    def testAddVertex(self):

        status = None

        try:
            self.testGraph.addVertex('A', 'A', 1)
            self.testGraph.addVertex('B', 'B', 2)
            self.testGraph.addVertex('C', 'C', 1)
            self.testGraph.addVertex('D', 'D', 5)
            self.testGraph.addVertex('E', 'E', 1)
            status = True

        except Exception:
            status = False

        return status

    def testAddEdge(self):

        status = None

        try:
            self.testGraph.addEdge('A', 'B', 'T', '10')
            self.testGraph.addEdge('A', 'C', 'T', '10')
            self.testGraph.addEdge('A', 'D', 'T', '10')
            self.testGraph.addEdge('B', 'D', 'T', '10')
            self.testGraph.addEdge('B', 'A', 'T', '10')
            self.testGraph.addEdge('C', 'A', 'T', '10')
            self.testGraph.addEdge('C', 'D', 'T', '10')
            self.testGraph.addEdge('D', 'B', 'T', '10')
            self.testGraph.addEdge('D', 'C', 'T', '10')
            self.testGraph.addEdge('D', 'E', 'T', '10')
            status = True

        except Exception:
            status = False

        return status

    def testDisplayVertices(self):

        status = None

        try:
            self.testGraph.displayVertices()
            status = True

        except Exception:
            status = False

        return status

    def testDisplayEdges(self):

        status = None

        try:
            self.testGraph.displayEdges()
            status = True

        except Exception:
            status = False

        return status

    def testDisplayAdjacentVertices(self):

        status = None

        try:
            self.testGraph.displayAdjacentVertices()
            status = True

        except Exception:
            status = False

        return status

    def testUpdateVertex(self):

        status = None

        try:
            self.testGraph.updateVertex('D', 'Z', 'Dog', 10)
            self.testGraph.updateVertex('C', 'D')
            status = True

        except Exception:
            status = False

        return status

    def testUpdateEdge(self):

        status = None

        try:
            self.testGraph.updateEdge("A", "B", 'Cat', 100)
            self.testGraph.updateEdge("B", 'A', 'Cat', 100)
            self.testGraph.updateEdge("D", 'B', None, 100)
            self.testGraph.updateEdge("B", 'D', 'Bush', None)
            status = True

        except Exception:
            status = False

        return status

    def testDisplayGraph(self):

        status = None

        try:
            self.testGraph.displayGraph()
            status = True

        except Exception:
            status = False

        return status

    def testDepthFirstSearch(self):

        self.testGraph = None
        self.testGraph = DSAGraph()

        self.testGraph.addVertex('A', 'A', 1)
        self.testGraph.addVertex('B', 'B', 2)
        self.testGraph.addVertex('C', 'C', 1)
        self.testGraph.addVertex('D', 'D', 5)
        self.testGraph.addVertex('E', 'E', 1)

        self.testGraph.addEdge('A', 'B', '-', 10)
        self.testGraph.addEdge('B', 'A', '-', 10)
        self.testGraph.addEdge('B', 'C', '-', 10)
        self.testGraph.addEdge('B', 'D', '-', 10)
        self.testGraph.addEdge('C', 'B', '-', 10)
        self.testGraph.addEdge('C', 'E', '-', 10)
        self.testGraph.addEdge('D', 'B', '-', 20)
        self.testGraph.addEdge('D', 'E', '-', 30)
        self.testGraph.addEdge("E", "C", '-', 50)
        self.testGraph.addEdge("E", "D", '-', 10)

        status = None

        try:
            routes = self.testGraph.generateRoutes('A', 'E')
            for testItem in routes:
                print(testItem)
            status = True

        except Exception:
            status = False

        return status


def main():

    graph = TestGraph()

    numOfTests = 9
    numPassed = 0

    test1 = graph.testAddVertex()
    if test1 == True:
        print("Add Vertices: Passed")
        numPassed += 1
    if test1 == False:
        print("Add Vertices: Failed")

    print('---------------------------')
    test2 = graph.testAddEdge()
    if test2 == True:
        numPassed += 1
        print("Add Edges: Passed")
    if test2 == False:
        print("Add Edges: Failed")

    print('---------------------------')
    test3 = graph.testDisplayVertices()
    if test3 == True:
        numPassed += 1
        print("Display Vertices: Passed")
    if test3 == False:
        print("Display Vertices: Failed")

    print('---------------------------')
    test4 = graph.testDisplayEdges()
    if test4 == True:
        numPassed += 1
        print("Display Edges: Passed")
    if test4 == False:
        print("Display Edges: Failed")

    print('---------------------------')
    test5 = graph.testDisplayAdjacentVertices()
    if test5 == True:
        numPassed += 1
        print("Display Adjacent Vertices: Passed")
    if test5 == False:
        print("Display Adjacent Vertices: Failed")

    print('---------------------------')
    test8 = graph.testDisplayGraph()
    if test8 == True:
        numPassed += 1
        print("Display Graph: Passed")
    if test8 == False:
        print("Display Graph: Failed")

    print('---------------------------')
    test9 = graph.testDepthFirstSearch()
    if test9 == True:
        numPassed += 1
        print("Depth First Search: Passed")
    if test9 == False:
        print("Depth First Search: Failed")

    print('---------------------------')
    test6 = graph.testUpdateVertex()
    if test6 == True:
        numPassed += 1
        print("Update Vertex: Passed")
    if test6 == False:
        print("Update Vertex: Failed")

    print()
    print('---------------------------')
    test7 = graph.testUpdateEdge()
    if test7 == True:
        numPassed += 1
        print("Update Edge: Passed")
    if test7 == False:
        print("Update Vertex: Failed")

    print("\n<-------TEST SUMMARY------->")
    print(f"Tests Passed = {numPassed}/{numOfTests}")


if __name__ == "__main__":
    main()
