# Problem:

Extend the implementation of the solver for the N-queen problem by adding a new function
called is_solution() that receives as a parameter a candidate solution and checks if the
solution is valid (correct) or not. The candidate solution is in the form of a list of string,
indicating the position of the queens in the chessboard.
You can assume N=5.
You can change other functions if needed. Here is an example output for two candidate
solutions.

COLUMNS = "abcde"

NUM_QUEENS = len(COLUMNS)

ACCEPT = 1

CONTINUE = 2

ABANDON = 3


all_solutions = []

def solve(partial_sol):...

def examine(partial_sol):...

def attacks(p1, p2):...

def extend(partial_sol):...

def is_solution(candidate_solution):...

candidate_solution1 = ['d3', 'c1', 'e5', 'b4', 'a2']

candidate_solution2 = ['e4', 'a1', 'c5', 'd2', 'b1']

result1 = is_solution(candidate_solution1)

result2 = is_solution(candidate_solution2)

print("Candidate Solution 1:", result1)

print("Candidate Solution 2:", result2)

[Output]:

Candidate Solution 1: Valid!

Candidate Solution 2: Invalid!
