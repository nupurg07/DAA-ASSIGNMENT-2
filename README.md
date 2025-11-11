## TRAVELLING SALESPERSON (LCBB)
The Travelling Salesperson Problem (TSP) is a classic optimization challenge where a salesperson must visit a set of cities exactly once and return to the starting city, aiming to find the shortest possible route. 
The Reduced Cost Matrix method in the Least Cost Branch and Bound (LCBB) approach for solving the Travelling Salesman Problem calculates an approximate minimal cost (C^) by reducing the cost matrix through row and column reductions, which helps establish lower bounds on possible solutions to prune the search space effectively.
This reduction assigns zero cost to certain matrix elements by subtracting the row and column minimums, and the sum of these minimum values forms a base cost used iteratively during the algorithm to estimate the least cost of completing the route.
## Method for computing C^ of non-root and non-leaf nodes:
Let A be the reduced cost matrix of node R, S be a child of R and the tree edge <R,S> corresponds to including the edge <i,j> in the tree, then the reduced cost matrix of node ‘S’ as follows:
Change all entries of row ‘i’ and column ‘j’ of matrix A to infinity

Set A[i,j] to infinity 

Reduce all rows and columns in the resultant matrix except the rows and columns containing only infinity

If ‘r’ is the total amount subtracted during reduction then,
                       C^(S) = C^(R) + A[i,j] + r
