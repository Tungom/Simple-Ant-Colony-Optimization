#-------------------------------------------------------------
# Chia E Tungom (chemago99@yahoo.com)
# Dec 3 2020
#
# Simple Ant Colony Optimization Algorithm (SACO)
#--------------------------------------------------------------

import random

def NextNode(Connections, RouletteProb):
    
    """ takes a list of connections and corresponding Roulette probabilities
    and returns an one connetion from the list of connetions 
    
    connections: List of nodes
    RouletteProb: List corresponding node roulette probability
    returns: int Node choosen """
    
    r = random.random()
    for i in range(len(Connections)):
        if i == 0 and r <= RouletteProb[i]:
            return Connections[i]
        elif r > RouletteProb[i] and r <= RouletteProb[i+1]:
            return Connections[i+1]

# Eliminate Loops 
def Deloop(route):
    l = len(route)
    for i in range(l):
        for j in range(i+1,l):
            j = l+i-j
            if j < len(route) and route[i] == route[j]:          # list changes as loop is removed 
                # print("Delooping:  ", x)
                [route.remove(k) for k in route[i+1:j+1]]
                # print("Delooped to: ", x)
    return route

def Travel(costGraph, pheromoneGraph, source, destination, alpha = 1, dropout = False):
    """ takes a 
    - connection graph (costGraph) a square matrix, 
    - pheromone graph (pheromoneGraph) a square matrix same size as costGraph, 
    - takeoff point (source) and destination are the int Node number
    - alpha balances the pheromone influence 
    - dropout is a boolean True if want to randomly drop some nodes 
    Returns a complete tour as a List
    """
    
    route = [source]
    while source != destination:  
        Connections = [i for i,j in enumerate(costGraph[source]) if j>0]
        
        # --------DROPOUT------------------------------------------------
        if dropout == True and len(Connections) > 1:
            # print("Drop out Initiated")
            removals = [Connections.remove(i) for i in Connections if (random.random() < 0.10 and len(Connections)>1)]
        #-------------------------------------------------------------------------------    
        pheromoneIJS = [ pheromoneGraph[source][i]**alpha for i in Connections]
        ProbabilityIJS = [ i/sum(pheromoneIJS) for i in pheromoneIJS]
        RouletteProb = [ sum(ProbabilityIJS[:i+1]) for i in range(len(ProbabilityIJS)) ]
        source = NextNode(Connections, RouletteProb)
        route.append(source)
    
    return Deloop(route)

def Updatepheromone(route, pheromoneGraph, rho = 0.5, bycost = True ):
    """ takes a route and use it to add pheromone to arcs in the 
    route
    
    route : route taken
    pheromoneGraph: pheromone matrix
    rho : evaporation rate 
    bycost:  bolean if pheromone update depends on cost
    
    returns pheromone graph """
    
    if bycost == True:
        tau = 1/len(route)
    else:
        tau = 1
        
    for i in range(len(route)-1):
        pheromoneGraph[route[i]][route[i+1]] = (1-rho)*(pheromoneGraph[route[i]][route[i+1]]) + tau
        pheromoneGraph[route[i+1]][route[i]] = (1-rho)*(pheromoneGraph[route[i+1]][route[i]]) + tau

    return pheromoneGraph


def SACO(costGraph, takeoff, destination, Population = 8, alpha = 2, rho = 0, iterations = 100, dropout = False, bycost = True): 
    """ takes a costgraph, takeoff point, destination point and number of times to travel (iterations)
    and return a tour """
    
    length = len(costGraph)
    PRM = [[1/length for i in range(length)] for j in range(length)]
    Ants = {"Ant" + str(i+1): None for i in range(Population)}
    
    while iterations > 0:
        #--------------TRAVEL-----------------------------------------
        for ant in Ants:
            Ants[ant] = Travel(costGraph, PRM, takeoff, destination, alpha, dropout)
        #-------------UPDATE PHEROMONE--------------------------------
        for ant in Ants:
            PRM = Updatepheromone(Ants[ant], PRM, rho, bycost)
        #-------------------------------------------------------------
        iterations -= 1
        #print(Route)
    return {"Ants": Ants, "PRM":PRM}
