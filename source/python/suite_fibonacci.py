from time import time

def fibo(n):
    if n==0 or n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
    
assert fibo(5)==8, 'erreur de calcul'

def fibo_iteratif(n):
    i = 1
    fib_1 = 1
    fib_2 = 1
    while i <= n:
        fib_1,fib_2 = fib_2,fib_1+fib_2
        i +=1
    return fib_1

fibo_iteratif(3)

def fibo_mem(n):
    mem = [0]*(n+1)  #permet de créer un tableau contenant n+1 zéro
    return fibo_mem_c(n,mem)

def fibo_mem_c(n,m):
    if n==0 or n==1:
        m[n]=1
        return m[n]
    elif m[n]>0:
        return m[n]
    else:
        m[n]=fibo_mem_c(n-1,m) + fibo_mem_c(n-2,m)
        return m[n]
    
if __name__ == '__main__':
    import sys 
    sys.setrecursionlimit(6000)
    
    t_0 = time()
    print(fibo(20))
    t_1 = time()
    print(t_1-t_0)