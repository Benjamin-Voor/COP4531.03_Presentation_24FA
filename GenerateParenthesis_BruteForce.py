from ParenthesesChecker_BruteForce import ParenthesesChecker
# from itertools import combinations_with_replacement # I forgot the difference between combination and permutation
from itertools import permutations


def GenerateParenthesis_helper(n: int, debugg: bool = False):
    s: str = ""
    for i in range(n):
        s += '()' # Make parantheses to be shuffled
    if debugg: print(s)
    perm = permutations(s, n*2) # Generator of all permutations
    not_answer: list[str] = []
    answer: list[str] = []
    for count_comb, i in enumerate(perm): # Generate each permutation one at a time
        s = ""
        for char in i:
            s += char # e.g '(', ')' -> "()"
        if ParenthesesChecker(s) and not s in answer:
            # Check whether each closing parenthesis is to the right of its own respective opening parenthesis.
            answer.append(s)
        elif debugg:
            not_answer.append(s)
        if debugg: print(answer, not_answer)
    if debugg: print('answer:', answer)
    return answer


def GenerateParenthesis(n: int, debugg: bool = False):
    answer = GenerateParenthesis_helper(n)
    if not ParenthesesChecker(answer):
        # print("this is not skibidi.")
        print("Logic Error: Invalid answer.")
        return
    return answer