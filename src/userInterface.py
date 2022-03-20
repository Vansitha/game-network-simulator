# ******************************************************************************
# FILE: userInterface.py
# Author: Vansitha Induja Ratnayake
# PURPOSE: Contains ui elements which is required for the programs front end
# REFERENCE: None
# COMMENTS: None
# REQUIRES: sys and os modules
# LAST MOD: 16/10/21
# *****************************************************************************

import sys
import os


class UserInterface:

    def getRunMode(self):
        '''Gets the appropriate command line arguments required to run the program'''

        mode = None

        if len(sys.argv) < 2:
            self.usageInfo()

        elif sys.argv[1] == "-i" and len(sys.argv) <= 2:
            mode = sys.argv[1]

        elif sys.argv[1] == "-s" and len(sys.argv) == 4:
            mode = sys.argv[1]

        return mode

    def usageInfo(self):

        print("=============== Running Program ================")
        print("'-i' - Run in interactive mode")
        print("eg: python3 gameofcatz.py -i")
        print("\n'-s infile outfile' - Run in simulation mode")
        print("eg: python3 gameofcatz.py -s input.txt output.txt")

        print("\n=============== Program Usage ==================")
        print("Enter the character in round brackets ()")
        print("to enter a particular menu.")
        print("\nVersion: 1.0")

    def mainMenu(self):

        print("====== Interative Testing Environment ======\n")
        print("(1). Load input file")
        print("(2). Node operations")
        print("(3). Edge operations")
        print("(4). Parameter tweaks")
        print("(5). Display Graph")
        print("(6). Display World")
        print("(7). Generate routes")
        print("(8). Display routes")
        print("(9). Save network")
        print("(q). quit")

        userChoice = input("\nChoice: ").lower()

        return userChoice

    def fileLoadMenu(self):

        print("===== Read File =====")
        print("(t). Read text file")
        print('(s). Read serialized file')
        print('(m). Main Menu')
        userChoice = input("Choice: ").lower()

        return userChoice

    def fileLoad(self):

        print("===== Load File =====")
        filename = input("Enter file name: ")

        return filename

    def nodeOperations(self):

        print("===== Node Operations =====")
        print("(f). Find")
        print("(i). Insert")
        print("(d). Delete")
        print("(u). Update")
        print("(m). Main Menu")
        userChoice = input("Choice: ").lower()

        return userChoice

    def nodeOperationsFind(self):

        findVertex = input("\nFind Vertex: ")
        return findVertex

    def edgeOperations(self):

        print("===== Edge Operations =====")
        print("(f). Find")
        print("(a). Add")
        print("(r). Remove")
        print("(u). Update")
        print("(m). Main Menu")
        userChoice = input("Choice: ").lower()

        return userChoice

    def fromEdge(self):

        edge = input("\nFrom vertex: ")
        return edge

    def toEdge(self):

        edge = input("To vertex: ")
        return edge

    def parameterTweaks(self):
        print("===== Parameter Tweaks =====")
        print("(n). Display and update vertex parameters")
        print("(e). Display and update edge parameters")
        print("(m). Main menu")
        userChoice = input("Choice: ").lower()

        return userChoice

    def displayGraph(self):

        print("===== Display Graph =====")
        print("(d). Display adjacency matrix")
        print("(m). Main menu")
        userChoice = input("Choice: ").lower()

        return userChoice

    def displayWorld(self):

        print("===== Display World =====")
        print("(d). Display World")
        print("(m). Main Menu")
        userChoice = input("Choice: ").lower()

        return userChoice

    def generateRoutes(self):
        print("===== Generate Routes =====")
        print("(g). Generate all routes")
        print("(t). Update target vertex")
        print("(m). Main Menu")
        userChoice = input("Choice: ").lower()

        return userChoice

    def displayGeneratedRoutes(self):
        print("===== Display Generated Routes =====")
        print("(d). Display Routes")

        print("(m). Main Menu")
        userChoice = input("Choice: ").lower()

        return userChoice

    def saveNetwork(self):
        print("===== Save Network =====")
        print("(s). Save ")
        print("(m). Main Menu")
        userChoice = input("Choice: ").lower()

        return userChoice

    def getSaveNetworkFileName(self):
        print("===== Save Network =====")
        filename = input("Enter filename: ")

        return filename

    # * Common ui elements and functions
    def clearScreen(self):

        os.system("clear")

    def returnToMain(self):

        input("\nPress any key to return to main menu...")

    def continueOperation(self):

        input("Press any key to continue..")
