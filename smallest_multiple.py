

def no_of_extra_twos(limit):
        i=0
        for even_nos in range(4,limit,2):
            i+=1
        return i


def sol(num):
    sol= 1
    while num>1:
        if sol%num!=0:
            sol*=num
        num=num-1
    return sol
#print(no_of_extra_twos(10))
print(sol(10))