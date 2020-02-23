import numpy as np 
def palindromo(c):
    return int(str(c)[::-1]) == c
n = 0
for a in np.arange(999,99,-1):
    for b in np.arange(a,99,-1):
        c = a * b
        if palindromo(c) and c > n:
            n = c
print(n)
