def multiply(a, b):
    if b < a:
        a, b = b, a

    def helper(a, b):
        if a == 0:
            return 0
        if a == 1:
            return b

        s = a >> 1
        side1 = helper(s, b)
        if a % 2 == 0:
            side2 = side1
        else:
            side2 = helper(a-s, b)
        return side1+side2

    return helper(a, b)

print(multiply(8, 7))