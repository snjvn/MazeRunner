#the maze is a graph (as in graph theory)
from queue import PriorityQueue
#0 - North
#1 - East
#2 - South
#3 - West
destinationSquare = [(8, 8), (8, 9), (9, 8), (9, 9)]
state  = (1, 1, 3, 0) #initialisation of state: x, y, quadrant, facing-direction

crossRoads = [(1, 1)] # list of all junctions. Or, we may say, list of all nodes of our graph. start square is added by default.

def h(loc, quad): #heuristic distance- calculated as manhattan distance
    if quad == 3:
        return abs(8-loc[0]) + abs(8-loc[1])
    if quad == 4:
        return abs(9-loc[0]) + abs(8-loc[1])
    if quad == 1:
        return abs(9-loc[0]) + abs(9-loc[1])
    if quad == 2:
        return abs(8-loc[0]) + abs(9-loc[1])

def openDirections(): #reads from ultrasound sensors, returns the list of open directions.
    pass

def moveOne(ST):# micromouse moves one unit IN THE DIRECTION IT IS CURRENTLY FACING
    pass

def UTurn():
    pass

def isDestination(ST):
    if (ST[0], ST[1]) in destinationSquare:
        return True #if final square is reached.
    else:
        return False #if final Square is not reached

ToDoList = PriorityQueue() # list of paths which are to be explored
while (not ToDoList.empty()) or ((state[0], state[1]) not in destinationSquare):
    if isDestination(state):
        print('reached')
        break
    if openDirections().length() > 1: #if there are multiple open-directions...
        #append to ToDoList
        #append (x, y) location to the crossRoads list
        pass

    elif openDirections().length() == 1: #only one direction to move
        moveOne(state)
    
    else:
        UTurn()
        #and then, navigate back to most recent junction or turning point - crossRoads[-1]
        #remove the deadend from ToDoList
        #take next from ToDoList
