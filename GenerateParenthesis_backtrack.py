def generateParenthesis_backtrack(n):
    array = []

    def backtrack(combo, openPar, closePar):
        if closePar == n:  # If all the parentheses have been used, add it to the array
            array.append(combo)
            return

        if openPar < n:  # Adds an open parentheses whenever possible
            backtrack(combo + "(", openPar + 1, closePar)

        if closePar < openPar:  # Adds a close parentheses whenever possible
            backtrack(combo + ")", openPar, closePar + 1)

    backtrack("", 0, 0)
    return array


if __name__ == '__main__':
    n = input('n = ')
    try:
        n = int(n)
    except ValueError:
        print("Error. Input value must be an integer.")

    if isinstance(n, int):
        if n >= 1:
            if n <= 8:
                generateParenthesis(n)
            else:
                print("Error. Input value must be at most 8.")
        else:
            print("Error. Input value must be at least 1.")