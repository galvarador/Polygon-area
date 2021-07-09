


def polygon(n):

    if n == 0:
        A= 0
    else:   
        A= 1 +((n-1)*n)*2

    return A


n= 0
AA = polygon(n)
print(AA) 
