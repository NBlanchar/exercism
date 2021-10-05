def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if(a > 0 or b > 0 or c > 0):
        if(a == b and a == c):
            return True
        else:
            return False
    else:
        return False


def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if(a + b > c and a + c > b and c + b > a):
        if(a > 0 or b > 0 or c > 0):
            if(a == b or a == c or b == c):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if(a + b > c and a + c > b and c + b > a):
        if(a > 0 or b > 0 or c > 0):
            if(a != b and a != c):
                return True
            else:
                return False
        else:
            return False
    return False
