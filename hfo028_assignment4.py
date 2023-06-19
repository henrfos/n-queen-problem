COLUMNS = "abcde"
NUM_QUEENS = len(COLUMNS)
ACCEPT = 1
CONTINUE = 2
ABANDON = 3
all_solutions = []

def solve(partial_sol):
    exam = examine(partial_sol)

    if exam == ACCEPT:
        print(partial_sol)

    elif exam != ABANDON:
        for p in extend(partial_sol):
            solve(p)


def examine(partial_sol):
    for i in range(len(partial_sol)):
        for j in range(i + 1, len(partial_sol)):
            if attacks(partial_sol[i], partial_sol[j]):
                return ABANDON

    if len(partial_sol) == NUM_QUEENS:
        return ACCEPT
    else:
        return CONTINUE
        

def attacks(p1, p2):
    column1 = COLUMNS.index(p1[0]) + 1
    row1 = int(p1[1])

    column2 = COLUMNS.index(p2[0]) + 1
    row2 = int(p2[1])

    return (row1 == row2 or
            column1 == column2 or
            abs(row1-row2) == abs(column1-column2))

def extend(partial_sol):
    results = []
    row = len(partial_sol) + 1

    for column in COLUMNS:
        new_solution = list(partial_sol)
        new_solution.append(column + str(row))
        results.append(new_solution)

    return results

def is_solution(candidate_solution):
    if examine(candidate_solution) == ACCEPT:
        return "Valid!"
    else:
        return "Invalid!"


candidate_solution1 = ['d3', 'c1', 'e5', 'b4', 'a2']
candidate_solution2 = ['e4', 'a1', 'c5', 'd2', 'b1']
result1 = is_solution(candidate_solution1)
result2 = is_solution(candidate_solution2)
print("Candidate Solution 1:", result1)
print("Candidate Solution 2:", result2)



