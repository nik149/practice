def check(p,q,x,y):
    if p < x or q < y:
        return False

    if p > q:
        p = p - q
    else:
        q = q - p

    if p == x and q == y:
        return True
    else:
        return check(p,q,x,y)

if __name__ == '__main__':
    x,y = map(int, raw_input().split(" "))

    p,q = map(int, raw_input().split(" "))

    print check(p,q,x,y)
