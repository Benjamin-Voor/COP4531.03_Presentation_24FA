

def ParenthesesChecker_stringHelper(s: str):
    s = s.lower()
    if s.endswith('('):
        return False
    tally: int = 0
    for char in s:
        if char == '(' and char == ')':
            print('erm, what the sigma?')
        elif char == '(':
            tally+=1
        elif char== ')':
            tally-=1
        if tally < 0:
            return False
    if tally == 0:
        return True
    elif tally != 0:
        return False
    else:
        print('erm, what the literal sigma?')

def ParenthesesChecker(var: any, debugg: bool = False) -> bool:
    s: str
    if type(var) == str:
        return ParenthesesChecker_stringHelper(var)
    elif type(var) == list[str] or type(var) == list:
        for s in var:
            if not ParenthesesChecker_stringHelper(s):
                return False
        if debugg: print(var, "is good -- ParenthesesChecker")
        return True
    else:
        print("Invalid input to ParanthesesChecker function. Input is type", type(var))
