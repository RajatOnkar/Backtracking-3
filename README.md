# Backtracking-3

## Problem1 
N Queens(https://leetcode.com/problems/n-queens/)

# Initialize a board of rows and columns equal to n and a result array to store the result.
# Backtracking - Initialize a list of board length and when the value is True we append the list by 'Q' 
# or else '.'.Terminate when the row index reaches the length of the board.
# For each column value we will iterate to see if another 'Q' exists or not using the isSafe function.
# isSafe function - Check the values in the board matrix by going over left, right and diagonal
# directions to see if there is a Queen 'Q' (to see if its safe to place the Queen)
# Return the list of strings where the Queen is placed.


## Problem2
Word Search(https://leetcode.com/problems/word-search/)

# Parse through the board by going over every element and use a backtrack function to find the word.
# Backtrack - Check if board element is start of the word, parse through the element neighbors to see 
# if we find the next character in the word. Parse till we get all the characters of the word else we
# will backtrack till we complete all 4 directions.
# Whenever the out of bounds condition or the word completes we will return. If word pattern is found 
# return 'True' else 'False'.