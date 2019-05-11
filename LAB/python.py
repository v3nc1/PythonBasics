def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    min_n=0
    max_n=0

    if a>b:
        max_n=a
        min_n=b
        if b==1:
            return 1
        elif b==0:
            return a
        else:
            return gcdRecur(b,a%b)
    else:
        max_n=b
        min_n=a
        if b==1:
            return 1
        elif b==0:
            return a
        else:
            return gcdRecur(b,a%b)


print(gcdRecur(273, 195))
