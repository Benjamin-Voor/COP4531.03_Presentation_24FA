from ParenthesesChecker_BruteForce import ParenthesesChecker
from GenerateParenthesis_BruteForce import GenerateParenthesis
from GenerateParenthesis_backtrack import generateParenthesis_backtrack

if __name__ == '__main__':
    debugg : bool = False
    if debugg:
        s: str = input("What is your parentheses? ")
        print(ParenthesesChecker(s))
    n: int = int(input("Brute Force input: "))
    print("Brute-force output: ", GenerateParenthesis(n, debugg))
    n = input("Backtracking input: ")
    try:
        n = int(n)
    except ValueError:
        print("Error. Input value must be an integer.")

    if isinstance(n, int):
        if n >= 1:
            if n <= 8:
                print("Backtracking output:", generateParenthesis_backtrack(n))
            else:
                print("Error. Input value must be at most 8.")
        else:
            print("Error. Input value must be at least 1.")