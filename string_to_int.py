def string_to_int(n: str) -> int:
    try:
        n = int(n)
        return n
    except ValueError:
        print("Error. Input value must be an integer.")