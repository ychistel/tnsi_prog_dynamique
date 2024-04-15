cpt = 0

def fibo_mem(n):
    m = [0]*(n+1)
    return fibo_mem_dyn(n,m)

def fibo_mem_dyn(n,m):
    global cpt
    if n == 0:
        return 0
    elif n==1:
        m[1] = 1
        return m[1]
    else:
        if m[n] > 0:
            return m[n]
        else:
            cpt += 1
            a = fibo_mem_dyn(n-1,m)
            cpt += 1
            b = fibo_mem_dyn(n-2,m)
            m[n] = a + b
            print(m)
            return m[n] 
    
def fibonnacci(n):
    global cpt
    print(f"appel recursif {cpt}")
    if n==0 or n==1:
      return n
    else:
        cpt += 1
        a = fibonnacci(n-1)
        cpt += 1
        b = fibonnacci(n-2)
        return a + b
    
terme = fibonnacci(20)
#terme = fibo_mem(100)