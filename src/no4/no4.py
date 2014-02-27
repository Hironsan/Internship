def minus(a, b):
    return a + (-b)

def multiply(a, b):
    if a < 0 and b < 0:
        return sum(-a for i in range(-b))
    if b < 0:
        a, b = b, a
        return sum(a for i in range(b))
    return sum(a for i in range(b))

def divide(a, b):
    cnt = 0
    if a > 0 and b > 0:
        while minus(a, b) >= 0:
            cnt += 1
            a = minus(a,b)
    elif a < 0 and b > 0:
        pass
    elif a > 0 and b < 0:
        pass
    else:
        a, b = -a, -b
        while minus(a, b) >= 0:
            cnt += 1
            a = minus(a, b)
    return cnt


if __name__ == "__main__":
    print multiply(-3,-5) == 15
    print multiply(-3,5) == -15
    print multiply(3,-5) == -15
    print multiply(3,5) == 15
    print multiply(-3,0) == 0
    print divide(8, 4) == 2
    print divide(3, 4) == 0
    print divide(-8, -4) == 2
    print divide(-7, -4) == 1