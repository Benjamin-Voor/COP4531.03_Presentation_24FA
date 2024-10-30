def parentheses_checker(s: str, debugg=False):
    s = s.lower() # Makes it easier to compare strings
    tally: int = 0
    for char in s: # For every parenthesis (singular) in the parentheses (plural)...
        if char == '(' and char == ')':
            if debugg: print('erm, what the sigma?') # Impossible result requires impossible print statement
        elif char == '(': # Increment for open parenthesis
            tally+=1
        elif char== ')': # Decrement for closed parenthesis
            tally-=1
        else:
            print('Invalid input!') # Outputted for anything other than parentheses
            return False
        if debugg: print('found', char, '\ttally', tally)
    if tally == 0:
        return True
    elif tally != 0:
        return False
    else:
        if debugg: print('erm, what the literal sigma?') # Impossible result requires impossible print statement