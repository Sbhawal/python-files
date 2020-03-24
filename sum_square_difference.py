def sq_of_sum(n):
    sum= n*(n + 1)*(2*n + 1) / 6
    return sum

def sum_of_sq(n):
    sum=n*(1+n)/2
    return sum**2

def diff(n):
    sol= sum_of_sq(n)-sq_of_sum(n)
    return sol



print(diff(100))

