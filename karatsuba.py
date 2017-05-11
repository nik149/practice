def mult(x,y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y

    n = max(len(str(x)), len(str(y)))
    nby2 = n / 2

    a = x / 10**(nby2)
    b = x % 10**(nby2)
    c = y / 10**(nby2)
    d = y % 10**(nby2)

    ac       = mult(a,c)
    bd       = mult(b,d)
    adplusbc = mult(a+b, c+d) - ac - bd ##(a + b)*(c + d)

    #ad = mult(x/(10**(n/2)), y%(10**(n/2)))
    #bc = mult(x%(10**(n/2)), y/(10**(n/2)))

    return (10**(2*nby2))*ac + (10**(nby2))*(adplusbc) + bd

if __name__ == '__main__':
    a = input()
    b = input()

    print "The product is: "
    print mult(a,b)
