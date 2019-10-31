
# N X N chess board
#input param= integer N
#output: all solutions for the problem
#DFS: Nodes-  correspond to partial configurations of queens on the first i rows
#Root node has no queens. Its children only have queens in the first row. 
#Each node can be represented as a list of columns that correspond 
#to the positions of queens in successive rows. 
#Implement the following two versions of the program for N=4 to 8
# Report the time taken to solve the problems of N sizes in a table and a plot.
# a) Exhaustive search: Search the tree exhaustively and report all solutions to the problem. 
# Call this function E_Queens. 
# b) Backtracking search: Terminate the recursion under a node if any two queens already 
# attack each other in that node. You must still return all solutions. 
# Call this function B_Queens.

import time

def E_Queens(N):
	finalSol =[]
	interim = []
	row = 0
	for n in range(N):
		interimValid= exhaustiveSearch(n, N, interim, row, True)
		for i in interimValid:
			finalSol.append(i)
	return finalSol

def exhaustiveSearch(n, N, interim, row, isValid):
	finalSol =[]

	if row == 0:
		interim = []
	#append node n to the interim path
	interim.append(n)

	if (row == N-1):
		if isValid:
			finalSol.append(interim)
		return finalSol

	for c in range(N):
		interimValid = isValid
		if interimValid:
			parent = -1
			for p in interim:
				parent += 1
				if p == c or (abs(p-c) == (row+1-parent)):
					interimValid = False
					break

		path = interim[:]
		# print(path)
		intVal = exhaustiveSearch(c, N, path, row+1, interimValid)

		for j in intVal:
			if len(j) >0:
				finalSol.append(j)
	return finalSol


def B_Queens(N):
	finalSol = []
	return backtrackingSearch(list(), N, finalSol)
	

def backtrackingSearch(board, N, finalSol):
	row = len(board)
	# print(row)
	if row == N and board != []:
		# print(board)
		finalSol.append(board)
	else:
		for q in range(N):
			if isValid(board, q):
				backtrackingSearch(board + [q], N, finalSol)
				# print("[q] is", [q])
	return finalSol

def isValid(board, q):
	i = len(board)
	j = q
	
	for pos, q in enumerate(board):
		#Is queen getting attacked by diagonals?
		if pos + q == i + j or pos - q == i-j:
			return False
		#Is queen already present in same row/col
		if pos == i or q == j:
			return False
	return True

def getOutput(N):
	start = time.clock()
	o1 = E_Queens(N)
	diff_E = time.clock()-start
	begin = time.clock()
	o2 = B_Queens(N)
	diff_B = time.clock()-begin 
	return o1, diff_E, o2, diff_B

# print(getOutput(4))




