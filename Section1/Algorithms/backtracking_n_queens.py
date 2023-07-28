import sys

class Solution:

    def solveNQueens(self, n: int):
        solutions = []
        state = []
        self.search(state, solutions, n)
        return solutions
        
    def is_valid_state(self, state, n):
        # check if it is a valid solution
        return len(state) == n

    def get_candidates(self, state, n):
        if not state:
            return range(n)
        
        # find the next position in the state to populate
        position = len(state)
        candidates = set(range(n))
        # prune down candidates that place the queen into attacks
        for row, col in enumerate(state):
            # discard the column index if it's occupied by a queen
            candidates.discard(col)
            dist = position - row
            # discard diagonals
            candidates.discard(col + dist)
            candidates.discard(col - dist)
        return candidates

    def search(self, state, solutions, n):
        if self.is_valid_state(state, n):
            state_string = self.state_to_nested_list(state, n)
            solutions.append(state_string)
            return

        for candidate in self.get_candidates(state, n):
            # recurse
            state.append(candidate)
            self.search(state, solutions, n)
            state.pop()
    
    def state_to_nested_list(self, state, n):
        # ex. [1, 3, 0, 2]
        # output: [[0, 1], [1, 3], [2, 0], [3, 2]]
        answer = []
        for index, value in enumerate(state):
            answer.append([index, value])
        return answer


arg = sys.argv
try:
    arg_1 = int(sys.argv[1])
except (ValueError, TypeError):
    print("N must be a number")
except IndexError:
    print("Usage: nqueens N")
else:
    if arg_1 < 4:
        print("N must be at least 4")
    else:
        NQueen = Solution()
        solution_list = NQueen.solveNQueens(int(sys.argv[1]))
        for solution in solution_list:
            print(solution)