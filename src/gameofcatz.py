# *****************************************************************
# FILE: gameofcatz.py
# Author: Vansitha Induja Ratnayake
# PURPOSE: Main program file connects all the functionality together
# REFERENCE: -
# COMMENTS: Requires command line arugments to run program
# REQUIRES: userInterface.py, createNetwork.py, sys module and
#           timeit module
# LAST MOD: 16/10/21
# *****************************************************************

import sys
import timeit
from userInterface import UserInterface
from createNetwork import BuildNetwork

ui = UserInterface()
mode = ui.getRunMode()
quitCode = 'quit'
programStatus = 'run'
fileLoaded = False
generatedRoutes = None
graphNetwork = BuildNetwork()

# * Running in interative mode
if mode == "-i":

    while (programStatus != quitCode):
        ui.clearScreen()
        userChoice = ui.mainMenu()
        ui.clearScreen()

        # * Runs process selected by the user from the program menu
        # * Choice 1 = Loading a file operation
        if userChoice == '1':

            runOperation1 = True

            while runOperation1:
                ui.clearScreen()
                fileOperationMode = ui.fileLoadMenu()

                # * Read text file
                if fileOperationMode == 't':
                    ui.clearScreen()
                    filename = ui.fileLoad()
                    working = graphNetwork.readFile(filename)
                    generatedRoutes = None  # * if a new file is loaded previous routes are erased

                    if working == True:
                        print("\nFile Loaded Successfully")
                        fileLoaded = True
                        runOperation1 = False
                        ui.returnToMain()
                    else:
                        input('\nPress any key to try again!')
                        ui.clearScreen()

                # * Read serialized file
                if fileOperationMode == 's':
                    ui.clearScreen()
                    filename = ui.fileLoad()
                    working = graphNetwork.readSerializedFile(filename)
                    generatedRoutes = None  # * if a new file is loaded previous routes are erased

                    if working == True:
                        print("File Loaded Successfully")
                        fileLoaded = True
                        runOperation1 = False
                        ui.returnToMain()
                    else:
                        input('\nPress any key to try again!')
                        ui.clearScreen()

                # * Return back to the main menu
                if fileOperationMode == 'm':
                    runOperation1 = False

        # * Choice 2 = Node operations
        if userChoice == '2':
            runOperation1 = True

            while runOperation1:
                ui.clearScreen()

                if fileLoaded == True:
                    nodeOperationMode = ui.nodeOperations()

                    # * Find a node operations
                    if nodeOperationMode == 'f':
                        vertex = ui.nodeOperationsFind()
                        print(f"\n{graphNetwork.network.getVertex(vertex)}")
                        print()
                        ui.continueOperation()
                        ui.clearScreen()

                    # * Insert a node operation
                    if nodeOperationMode == 'i':
                        label = input("\nEnter Label: ")
                        displayLabel = input("Enter display label: ")
                        value = input("Enter value: ")
                        graphNetwork.network.addVertex(
                            label, displayLabel, value)
                        print()
                        ui.continueOperation()
                        ui.clearScreen()

                    # * Delete a node operation
                    if nodeOperationMode == 'd':
                        print("\nDelete feature is unavailable at the moment\n")
                        ui.continueOperation()
                        ui.clearScreen()

                    # * Update a node opeartion
                    if nodeOperationMode == 'u':

                        previouslabel = input("Update vertex of: ")
                        newLabel = input("Update vertex to: ")
                        displayLabel = input("New display label (optional): ")
                        newValue = input("New value (optional): ")
                        print()

                        if displayLabel == '':
                            displayLabel = None
                        if newValue == '':
                            newValue = None

                        graphNetwork.network.updateVertex(
                            previouslabel, newLabel, displayLabel, newValue)

                        print()
                        ui.continueOperation()
                        ui.clearScreen()

                    # * Return back to menu operation
                    if nodeOperationMode == 'm':
                        runOperation1 = False
                else:
                    print('Load file first to perform node operations!')
                    ui.returnToMain()
                    runOperation1 = False

        # * Menu to perform edge operations
        # * Choice 3 = edge opeartions
        if userChoice == '3':

            runOperation3 = True

            while runOperation3:
                ui.clearScreen()

                if fileLoaded == True:
                    edgeOperationMode = ui.edgeOperations()

                    # * Find an edge
                    if edgeOperationMode == 'f':
                        fromV = ui.fromEdge()
                        toV = ui.toEdge()
                        print(f"\n{graphNetwork.network.getEdge(fromV, toV)}\n")
                        ui.continueOperation()
                        ui.clearScreen()

                    # * Add a new edge
                    if edgeOperationMode == 'a':
                        fromVertex = ui.fromEdge()
                        toVertex = ui.toEdge()
                        label = input("Label: ")
                        value = input("Value: ")

                        graphNetwork.network.addEdge(
                            fromVertex, toVertex, label, value)

                        print()
                        ui.continueOperation()
                        ui.clearScreen()

                    # * Remove an edge
                    if edgeOperationMode == 'r':
                        print("\nRemove feature is unavailable at the moment\n")
                        ui.continueOperation()
                        ui.clearScreen()

                    # * Update an edge
                    if edgeOperationMode == 'u':
                        fromVertex = ui.fromEdge()
                        toVertex = ui.toEdge()
                        updateLabel = input("Update Label: ")
                        updateValue = input("Update Value: ")

                        print()
                        graphNetwork.network.updateEdge(
                            fromVertex, toVertex, updateLabel, updateValue)

                        print()
                        ui.continueOperation()
                        ui.clearScreen()

                    # * Return back to the menu
                    if edgeOperationMode == 'm':
                        runOperation3 = False

                else:
                    print('Load file first to perform edge operations!')
                    ui.returnToMain()
                    runOperation3 = False

        # * Parameter tweaks
        # * Choice 4 = parameter tweaks
        if userChoice == '4':

            runOperation4 = True

            while runOperation4 == True:
                ui.clearScreen()

                if fileLoaded == True:
                    parameterTweaksMode = ui.parameterTweaks()

                    # * Node parameter tweaks
                    if parameterTweaksMode == 'n':
                        print("\nVertex Parameters\n")

                        # * Display (e)nteries only in the hash table
                        graphNetwork.nodeCodeHashTable.display('e')
                        option = input("\nUpdate parameter? (y/n): ").lower()

                        if option == 'y':
                            parameterKey = input("Edit Value of: ")
                            parameterValue = input("Enter new value: ")
                            graphNetwork.nodeParameterTweaks(
                                parameterKey, parameterValue)

                            print()
                            ui.continueOperation()
                            ui.clearScreen()

                        if option == 'n':
                            print()
                            ui.continueOperation()
                            ui.clearScreen()

                    # * Edge parameter tweaks
                    if parameterTweaksMode == 'e':
                        print("\n Edge Parameters \n")

                        # * Display entries only
                        graphNetwork.edgeCodeHashTable.display('e')
                        option = input("\nUpdate parameter? (y/n): ").lower()

                        if option == 'y':
                            parameterKey = input("Edit Value of: ")
                            parameterValue = input("Enter new value: ")
                            graphNetwork.edgeParameterTweaks(
                                parameterKey, parameterValue)

                            print()
                            ui.continueOperation()
                            ui.clearScreen()

                        if option == 'n':
                            print()
                            ui.continueOperation()
                            ui.clearScreen()

                    # * Return to main menu
                    if parameterTweaksMode == 'm':
                        runOperation4 = False

                else:
                    print("Load file first to perform parameter tweaks!")
                    ui.returnToMain()
                    runOperation4 = False

        # * Display graph as a weighted adjacency matrix
        # * Choice 5 = display graph
        if userChoice == '5':

            runOperation5 = True

            while runOperation5:
                ui.clearScreen()
                if fileLoaded == True:
                    displayOperationMode = ui.displayGraph()

                    # * display graph option
                    if displayOperationMode == 'd':
                        print('\n0 = No Edge')
                        print('N = Vertex not connected to graph\n')
                        graphNetwork.network.displayGraph()
                        rawGraph = graphNetwork.network.generateGraphMatrix()
                        print()
                        save = input("\nSave Graph? (y/n): ")
                        if save == 'y':
                            filename = input("Save as: ")
                            working = graphNetwork.saveGraph(
                                rawGraph, filename)

                            if working == True:
                                print(f"Saved graph to {filename}\n")
                                ui.continueOperation()
                                ui.clearScreen()

                            if working == False:
                                print(f"Could not save graph to {filename}\n")
                                ui.continueOperation()
                                ui.clearScreen()

                        if save == 'n':
                            ui.continueOperation()
                            ui.clearScreen()

                    # * Return to menu option
                    if displayOperationMode == 'm':
                        runOperation5 = False

                else:
                    print("Load file first to display graph!")
                    ui.returnToMain()
                    runOperation5 = False

        # * Display world
        # * Choice 6 = display world
        if userChoice == '6':

            runOperation6 = True

            while runOperation6:
                ui.clearScreen()
                if fileLoaded == True:
                    displayOperationMode = ui.displayWorld()

                    # * display world option
                    if displayOperationMode == 'd':
                        print()
                        graphNetwork.displayNetwork()
                        vertexCount = graphNetwork.network.getVertexCount()
                        edgeCount = graphNetwork.network.getEdgeCount()
                        print(
                            f"\nNumber of objects in world (vertices): {vertexCount}")
                        print(f"Total Connections (edges): {edgeCount}")
                        option = input("\nSave to file? (y/n): ")

                        if option == 'y':
                            saveFilename = input("Save as: ")
                            working = graphNetwork.saveWorld(saveFilename)

                            if working == True:
                                print(f"World Saved to {saveFilename}")
                                print()
                                ui.continueOperation()

                            if working == False:
                                print(
                                    f"Could not save world to {saveFilename}")
                                ui.continueOperation()

                        if option == 'n':
                            ui.continueOperation()
                            ui.clearScreen()

                    # * Return to menu option
                    if displayOperationMode == 'm':
                        runOperation6 = False

                else:
                    print("Load file first to display world!")
                    ui.returnToMain()
                    runOperation6 = False

        # * Generate Routes
        # * Choice 7 = generate routes
        if userChoice == '7':

            runOperation7 = True

            while runOperation7:
                ui.clearScreen()
                if fileLoaded == True:
                    displayOperationMode = ui.generateRoutes()

                    # * Generate routes option
                    if displayOperationMode == 'g':
                        try:
                            print(
                                "Note: Routes may take longer to gernerate in some instances")
                            print("\nGenerating routes...")
                            startTime = timeit.default_timer()
                            generatedRoutes = graphNetwork.generateGraphRoutes()
                            endTime = timeit.default_timer()
                            totaltime = endTime - startTime
                            print("Success: Routes generated\n")
                            print(
                                f"Total time taken: {format(totaltime, '.3f')}s")

                        except Exception:
                            print("Failed to generate Routes!\n")
                            print()
                        ui.continueOperation()
                        ui.clearScreen()

                    # * Modify target vertex to any vertex in the graph
                    if displayOperationMode == 't':
                        print("\nUpdate Target Vertex\n")
                        print(
                            f"Current target vertex: {graphNetwork.targetNode}")
                        currentTarget = graphNetwork.targetNode
                        updateTarget = input("Update target vertex to: ")
                        graphNetwork.targetNode = updateTarget

                        if graphNetwork.network.hasVertex(updateTarget):
                            if graphNetwork.startNode != updateTarget:
                                graphNetwork.targetNode = updateTarget
                                print(
                                    f"New target vertex set to: {graphNetwork.targetNode}\n")
                            else:
                                print(
                                    "Target cannot be the same as start vertex!\n")
                                graphNetwork.targetNode = currentTarget
                        else:
                            graphNetwork.targetNode = currentTarget
                            print(f"Vertex {updateTarget} not in graph!\n")

                        ui.continueOperation()
                        ui.clearScreen()

                    # * Return to main menu
                    if displayOperationMode == 'm':
                        runOperation7 = False
                else:
                    print("Load file first to generate routes!")
                    ui.returnToMain()
                    runOperation7 = False

        # * Display Routes
        # * Choice 8 = display routes
        if userChoice == '8':

            runOperation8 = True
            while runOperation8:
                ui.clearScreen()

                # * if file is not loaded and routes are not generated cannot enter menu
                if fileLoaded == True:
                    if generatedRoutes != None:
                        displayOperationMode = ui.displayGeneratedRoutes()

                        # * display generated routes
                        if displayOperationMode == 'd':

                            routeCount = 0
                            for route in generatedRoutes:
                                print(route)
                                print()
                                routeCount += 1

                            print(f"\nTotal Routes: {routeCount}\n")
                            option = input("Save routes? (y/n): ").lower()

                            if option == 'y':
                                saveFilename = input("Save as: ")
                                working = graphNetwork.saveRoutes(
                                    generatedRoutes, saveFilename)

                                if working == True:
                                    print(f"\nSaved routes to {saveFilename}")
                                    ui.continueOperation()

                            if option == 'n':
                                ui.continueOperation()
                                ui.clearScreen()

                        # * Return to main menu
                        if displayOperationMode == 'm':
                            runOperation8 = False

                    else:
                        print("Generate Routes first!")
                        ui.returnToMain()
                        runOperation8 = False

                else:
                    print("Load file and generate routes to display routes!")
                    ui.returnToMain()
                    runOperation8 = False

        # * Save Network
        # * Choice 9 = save network
        if userChoice == '9':

            runOperation9 = True

            while runOperation9:
                ui.clearScreen()

                if fileLoaded == True:
                    displayOperationMode = ui.saveNetwork()

                    # * save network option (saves to a serialized file)
                    if displayOperationMode == 's':
                        ui.clearScreen()
                        filename = ui.getSaveNetworkFileName()
                        working = graphNetwork.saveToSerialized(filename)

                        if working == True:
                            print("\nNetowork saved successfully")
                            fileLoaded = True
                            runOperation1 = False
                            ui.returnToMain()
                        else:
                            print("An error occurred while saving network")
                            ui.returnToMain()
                            runOperation9 = False

                    if displayOperationMode == 'm':
                        runOperation9 = False

                else:
                    print("No loaded network to save!")
                    ui.returnToMain()
                    runOperation9 = False

        if userChoice == 'q':
            programStatus = quitCode

# * Running program in simulation mode
# * Note: Simulation mode accepts only text files to load serialized files use interative mode
if mode == "-s":

    inputFile = sys.argv[2]
    outputFile = sys.argv[3]
    working = graphNetwork.readFile(inputFile)

    try:
        if working == True:
            print("Generating Routes...")
            generatedRoutes = graphNetwork.generateGraphRoutes()
            graphNetwork.saveRoutes(generatedRoutes, outputFile)
            print("Routes Generated")
            print(f"Saved routes to {outputFile}")

    except Exception:
        print("An Error Occurred while generating routes")
