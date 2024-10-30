from ParenthesesChecker import parentheses_checker

def generate_parenthesis(debugg=False):
    if debugg:
        s: str = input("What is your parentheses? ")
        if parentheses_checker(s, debugg):
            print('that\'s on skibidi')
        else:
            print('that\'s cap')
    n: str = input('Please type the input \'n\', where 1 <= n <= 8: ')
    if n.isdigit():
        n: int = int(n)
        if 1 <= n <= 8:
            print('invalid input!', n, 'is too large or too small of a digit! \'n\' must be such that 1 <= n <= 8!')
    else:
        print('Invalid input!', n, 'is not a digit!')
        return
    if debugg: print('n is', n, 'and is a', type(n))
