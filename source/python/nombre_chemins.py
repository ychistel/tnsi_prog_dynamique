cpt0 = 0
cpt1 = 0

def nombre_chemins(n,p):
    global cpt0
    if n == 1 or p == 1:
        return 1
    else:
        cpt0 += 1
        h = nombre_chemins(n-1,p)
        cpt0 += 1
        v = nombre_chemins(n,p-1)
        return h + v 

def nb_chemins_mem(n,p):
    mem = [[0 for j in range(p)] for i in range(n)]
    return nb_chemins_rec(n,p,mem)

def nb_chemins_rec(n,p,mem):
    global cpt1
    if n == 1 or p == 1:
        mem[n-1][p-1]=1
        return 1
    if mem[n-1][p-1] > 0:
        return mem[n-1][p-1]
    else:
        cpt1 += 1
        h = nb_chemins_rec(n-1,p,mem)
        cpt1 += 1
        v = nb_chemins_rec(n,p-1,mem)
        mem[n-1][p-1] = h + v
        return mem[n-1][p-1]

nb0 = nombre_chemins(10,18)
nb = nb_chemins_mem(10,18)