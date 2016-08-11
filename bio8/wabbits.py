def wabbits(n,m): #n = number of months total m = life span(months)
    r = ['x'] + [1] + [0]*(m-1)
    for i in range(n-1):
        r = ['x'] + [sum(r[2:])] + r[1:-1]
    return sum(r[1:])
