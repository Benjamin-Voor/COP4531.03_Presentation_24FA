def ParenthesesChecker(s: str):
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
    if tally == 0:
        return True
    elif tally != 0:
        return False
    else:
        print('erm, what the literal sigma?')