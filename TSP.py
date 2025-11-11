import copy
import math
import heapq

def reduceMatrix(matrix):
    # Perform row and column reductions on the cost matrix
    reductionCost = 0
    for i in range(len(matrix)):
        row_min = min(matrix[i])
        if row_min != math.inf and row_min > 0:
            for j in range(len(matrix)):
                if matrix[i][j] != math.inf:
                    matrix[i][j] -= row_min
            reductionCost += row_min
    for j in range(len(matrix)):
        col = [matrix[i][j] for i in range(len(matrix))]
        col_min = min(col)
        if col_min != math.inf and col_min > 0:
            for i in range(len(matrix)):
                if matrix[i][j] != math.inf:
                    matrix[i][j] -= col_min
            reductionCost += col_min
    return matrix, reductionCost

def setRowToInfinity(matrix, row):
    # Set all elements in the specified row to infinity
    for j in range(len(matrix)):
        matrix[row][j] = math.inf

def setColumnToInfinity(matrix, col):
    # Set all elements in the specified column to infinity
    for i in range(len(matrix)):
        matrix[i][col] = math.inf

def TSP_LCBB(costMatrix):
    n = len(costMatrix)
    # Create initial reduced cost matrix and calculate its cost
    initialMatrix = copy.deepcopy(costMatrix)
    initialMatrix, initialCost = reduceMatrix(initialMatrix)
    bestCost = math.inf
    bestPath = []
    priorityQueue = []
    # Start from city 0 with initial reduced matrix and cost
    heapq.heappush(priorityQueue, (initialCost, (0,), initialMatrix))
    
    while priorityQueue:
        currentCost, currentPath, currentMatrix = heapq.heappop(priorityQueue)
        if len(currentPath) == n:
            # Complete route: add cost to return to start city
            totalCost = currentCost + costMatrix[currentPath[-1]][0]
            if totalCost < bestCost:
                bestCost = totalCost
                bestPath = list(currentPath) + [0]
        else:
            currentCity = currentPath[-1]
            for nextCity in range(n):
                if nextCity not in currentPath:
                    # Create child matrix for the next city branch
                    childMatrix = copy.deepcopy(currentMatrix)
                    setRowToInfinity(childMatrix, currentCity)
                    setColumnToInfinity(childMatrix, nextCity)
                    childMatrix[nextCity][0] = math.inf  # Avoid premature cycle
                    costTravel = currentMatrix[currentCity][nextCity]
                    # Reduce the child matrix and calculate additional cost
                    reducedChildMatrix, reductionCost = reduceMatrix(childMatrix)
                    totalChildCost = currentCost + costTravel + reductionCost
                    # Prune paths with cost exceeding current best cost
                    if totalChildCost < bestCost:
                        childPath = currentPath + (nextCity,)
                        heapq.heappush(priorityQueue, (totalChildCost, childPath, reducedChildMatrix))
    return bestPath, bestCost
import copy
import math
import heapq

def reduceMatrix(matrix):
    # Perform row and column reductions on the cost matrix
    reductionCost = 0
    for i in range(len(matrix)):
        row_min = min(matrix[i])
        if row_min != math.inf and row_min > 0:
            for j in range(len(matrix)):
                if matrix[i][j] != math.inf:
                    matrix[i][j] -= row_min
            reductionCost += row_min
    for j in range(len(matrix)):
        col = [matrix[i][j] for i in range(len(matrix))]
        col_min = min(col)
        if col_min != math.inf and col_min > 0:
            for i in range(len(matrix)):
                if matrix[i][j] != math.inf:
                    matrix[i][j] -= col_min
            reductionCost += col_min
    return matrix, reductionCost

def setRowToInfinity(matrix, row):
    # Set all elements in the specified row to infinity
    for j in range(len(matrix)):
        matrix[row][j] = math.inf

def setColumnToInfinity(matrix, col):
    # Set all elements in the specified column to infinity
    for i in range(len(matrix)):
        matrix[i][col] = math.inf

def TSP_LCBB(costMatrix):
    n = len(costMatrix)
    # Create initial reduced cost matrix and calculate its cost
    initialMatrix = copy.deepcopy(costMatrix)
    initialMatrix, initialCost = reduceMatrix(initialMatrix)
    bestCost = math.inf
    bestPath = []
    priorityQueue = []
    # Start from city 0 with initial reduced matrix and cost
    heapq.heappush(priorityQueue, (initialCost, (0,), initialMatrix))
    
    while priorityQueue:
        currentCost, currentPath, currentMatrix = heapq.heappop(priorityQueue)
        if len(currentPath) == n:
            # Complete route: add cost to return to start city
            totalCost = currentCost + costMatrix[currentPath[-1]][0]
            if totalCost < bestCost:
                bestCost = totalCost
                bestPath = list(currentPath) + [0]
        else:
            currentCity = currentPath[-1]
            for nextCity in range(n):
                if nextCity not in currentPath:
                    # Create child matrix for the next city branch
                    childMatrix = copy.deepcopy(currentMatrix)
                    setRowToInfinity(childMatrix, currentCity)
                    setColumnToInfinity(childMatrix, nextCity)
                    childMatrix[nextCity][0] = math.inf  # Avoid premature cycle
                    costTravel = currentMatrix[currentCity][nextCity]
                    # Reduce the child matrix and calculate additional cost
                    reducedChildMatrix, reductionCost = reduceMatrix(childMatrix)
                    totalChildCost = currentCost + costTravel + reductionCost
                    # Prune paths with cost exceeding current best cost
                    if totalChildCost < bestCost:
                        childPath = currentPath + (nextCity,)
                        heapq.heappush(priorityQueue, (totalChildCost, childPath, reducedChildMatrix))
    return bestPath, bestCost