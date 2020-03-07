def fatorial(num=1):
    f = 1
    for c in range(num,0,-1):
        f *= c
    return f
f1 = fatorial(1)
f2= fatorial(5)
f3= fatorial(8)
print(f1,f2,f3)