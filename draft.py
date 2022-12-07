from queue import PriorityQueue

destinationSquare = [(8, 8), (8, 9), (9, 8), (9, 9)]
state  = (1, 1, 3, 'N') #init state: x, y, quadrant, facing-direction
crossRoads = [(1, 1)]

def h(loc, quad):
    if quad == 3:
        return abs(8-loc[0]) + abs(8-loc[1])
    if quad == 4:
        return abs(9-loc[0]) + abs(8-loc[1])
    if quad == 1:
        return abs(9-loc[0]) + abs(9-loc[1])
    if quad == 2:
        return abs(8-loc[0]) + abs(9-loc[1])

def openDirections(): #reads from ultrasound, returns the open directions.
    pass

def moveOne():# micromouse moves one unit IN THE DIRECTION IT IS CURRENTLY FACING
    pass

def UTurn():
    pass

ToDoList = PriorityQueue() # list of paths which are to be explored
while (not ToDoList.empty()) or ((state[0], state[1]) not in destinationSquare):
    if openDirections().length() > 1: #if there are multiple open-directions...
        #append to ToDoList
        #append (x, y) location to the crossRoads list
        pass

    elif openDirections().length() == 1: #only one direction to move
        moveOne()
    
    else:
        UTurn()
        #and then, navigate back to most recent junction or turning point - crossRoads[-1]
        #remove the deadend from ToDoList
        #take next from ToDoList
