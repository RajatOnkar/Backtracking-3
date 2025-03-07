'''
// Time Complexity :
# Problem 1 - O(n!) where n is each row of the matrix
# Problem 2 - O(m*n * 2^L) where mxn is the size of the board and L the length of the word
// Space Complexity :
# Problem 1 - O(n*n) as all elements are appended in a list array and an extra parse on the board
# Problem 2 - O(L) L - is the recursive calls
// Did this code successfully run on Leetcode :
# Yes the code ran successfully.

// Any problem you faced while coding this :
# Problem 2 - got TIME LIMIT EXCEEDED... Please suggest !

// Your code here along with comments explaining your approach
'''
## Problem 1 - N Queens
# Initialize a board of rows and columns equal to n and a result array to store the result.
# Backtracking - Initialize a list of board length and when the value is True we append the list by 'Q' 
# or else '.'.Terminate when the row index reaches the length of the board.
# For each column value we will iterate to see if another 'Q' exists or not using the isSafe function.
# isSafe function - Check the values in the board matrix by going over left, right and diagonal
# directions to see if there is a Queen 'Q' (to see if its safe to place the Queen)
# Return the list of strings where the Queen is placed.

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [[0 for c in range(n)] for r in range(n)]
        result = []
        self.backtrack(board, 0, result)
        return result
    
    def backtrack(self, board, r, result):
        ##base
        if r == len(board):
            ## all queens are placed
            li = ['' for _ in range(len(board))]
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == True:
                        li[i] += 'Q'
                    else:
                        li[i] += '.'
            result.append(li)

        ##logic
        for c in range(len(board)):
            if self.isSafe(board, r, c):
                ## action
                board[r][c] = True
                ## recurse
                self.backtrack(board, r+1, result)
                ## backtrack
                board[r][c] = False
    
    def isSafe(self, board, r, c):
        ## column UP
        for i in range(r):
            if board[i][c] == True:
                return False
        i = r; j = c
        ## Diagonal UP LEFT
        while(i >= 0 and j >= 0):
            if board[i][j] == True:
                return False
            i -= 1; j -= 1
        ## Diagonal UP RIGHT
        i = r; j = c
        while(i >= 0 and j < len(board)):
            if board[i][j] == True:
                return False
            i -= 1; j += 1
        return True  

## Problem 2 - Word Search
# Parse through the board by going over every element and use a backtrack function to find the word.
# Backtrack - Check if board element is start of the word, parse through the element neighbors to see 
# if we find the next character in the word. Parse till we get all the characters of the word else we
# will backtrack till we complete all 4 directions.
# Whenever the out of bounds condition or the word completes we will return. If word pattern is found 
# return 'True' else 'False'.

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j]:
                    if self.backtrack(board, i, j, 0, word):
                        return True
        return False
    
    def backtrack(self, board, r, c, idx, word):
        dirs = [[-1,0], [1,0], [0,1], [0,-1]]
        ##base
        if r < 0 or c < 0 or r == len(board) or c == len(board[0]) or board[r][c] == '#':
            return False

        ##logic
        if board[r][c] == word[idx]:
            if idx == len(word)-1:
                return True
            ## action
            currChar = board[r][c]
            board[r][c] = '#'
        
            for dir in dirs:
                nr = r + dir[0]
                nc = c + dir[1]
                if self.backtrack(self, board, nr, nc, idx + 1, word):
                    return True
        ##backtrack
            board[r][c] = currChar
        return False 
