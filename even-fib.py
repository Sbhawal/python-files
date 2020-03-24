def sol(limit):
    a=0
    b=2
    t=2
    s=0
    while t<=limit:
        s=s+t
        t=a+4*b
        a=b
        b=t
    return s

print(sol(4000000))