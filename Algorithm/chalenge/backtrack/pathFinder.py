'''
implementation of backtracking
'''

def pathFinder(matrix, position, N) -> list:
# returns a list of the paths taken:
	if position == (N-1, N-1):
		return [ (N-1, N-1) ]
	x, y = position
	# move right
	if (x+1) < N and matrix[x+1][y] == 1:
		a = pathFinder(matrix, (x+1, y), N)
		if a != None:
            # backtrack to return the value
			return[position] + a

	# move down
	if (y+1) < N and matrix[x][y+1] == 1:
		b = pathFinder(matrix, (x, y+1), N)
		if b != None:
			return[position] + b

matrix = [[1, 1, 1, 1, 0], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [0, 1, 0, 0, 0], [1, 1, 1, 1, 1] ]

print (pathFinder(matrix, (0,0), 5))