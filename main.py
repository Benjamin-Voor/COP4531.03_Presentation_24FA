from ParenthesesChecker_BruteForce import ParenthesesChecker
from GenerateParenthesis_BruteForce import GenerateParenthesis
from GenerateParenthesis_backtrack import generateParenthesis_backtrack
from string_to_int import string_to_int


if __name__ == '__main__':
    debugg : bool = False
    skip: bool = False
    if not skip:
        if debugg:
            s: str = input("What is your parentheses? ")
            print(ParenthesesChecker(s))
        n: str = input("Brute Force input: ")
        n = string_to_int(n)
        print("Brute-force output: ", GenerateParenthesis(n, debugg))

    n = input("Backtracking input: ")
    n = string_to_int(n)
    if isinstance(n, int):
        if n >= 1:
            if n <= 8:
                print("Backtracking output:", generateParenthesis_backtrack(n, debugg))
            else:
                print("Error. Input value must be at most 8.")
        else:
            print("Error. Input value must be at least 1.")