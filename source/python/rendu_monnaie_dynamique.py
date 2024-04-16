unites = [20,10,5,2]

def rendu_monnaie_mem(somme_a_rendre):
    mem = [0]*(somme_a_rendre + 1)
    return rendu_monnaie_mem_rec(somme_a_rendre,mem)

def rendu_monnaie_mem_rec(somme_a_rendre,m):
    if somme_a_rendre == 0:
        return 0
    elif m[somme_a_rendre] > 0:
        return m[somme_a_rendre]
    else:
        mini = 1000
    for i in range(len(unites)):
        if unites[i] <= somme_a_rendre:
            nb = 1 + rendu_monnaie_mem_rec(somme_a_rendre - unites[i],m)
            if nb < mini:
                mini = nb
                m[somme_a_rendre] = mini
    return mini

n = rendu_monnaie_mem(587)