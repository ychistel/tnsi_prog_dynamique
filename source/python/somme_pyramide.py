from random import randint

def sous_pyramide_gauche(p):
    return [p[j][:-1] for j in range(1,len(p))]

def sous_pyramide_droite(p):
    return [p[j][1:] for j in range(1,len(p))]
    
def somme_pyramide(p):
    global cpt
    if len(p) == 1:
        return p[0][0]
    else:
        p_g = sous_pyramide_gauche(p)
        p_d = sous_pyramide_droite(p)
        cpt += 1
        s_g = somme_pyramide(p_g)
        cpt += 1
        s_d = somme_pyramide(p_d)
        return p[0][0] + max(s_g,s_d)

def somme_pyramide_mem(p):
    mem = [[0 for i in range(j)] for j in range(1,n+1)]
    return somme_pyramide_mem_rec(p,mem)

def somme_pyramide_mem_rec(p,mem):
    if len(p) == 1:
        mem[0][0] = p[0][0]
        return p[0][0]
    else:
        p_g = sous_pyramide_gauche(p)
        mem_g = sous_pyramide_gauche(mem)
        p_d = sous_pyramide_droite(p)
        mem_d = sous_pyramide_droite(mem)
        if mem_g[0][0] != 0:
            s_g = mem_g[0][0]
        else:
            s_g = somme_pyramide_mem_rec(p_g,mem_g)
        if mem_d[0][0] != 0:
            s_d = mem_d[0][0]
        else:
            s_d = somme_pyramide_mem_rec(p_d,mem_d)
        mem[0][0] = p[0][0] + max(s_g,s_d)
        print("mem:",mem)
        return p[0][0] + max(s_g,s_d)
    
def parcours_max_pyramide(p,chemin=[]):
    if len(p) > 1:
        p_g = sous_pyramide_gauche(p)
        p_d = sous_pyramide_droite(p)
        if somme_pyramide(p_g) >= somme_pyramide(p_d):
            chemin.append(p_g[0][0])
            parcours_max_pyramide(p_g,chemin)
        else:
            chemin.append(p_d[0][0])
            parcours_max_pyramide(p_d,chemin)
    # on ajoute le sommet de la pyramide
    chemin = p[0] + chemin
    return chemin
    
if __name__ == '__main__':
    cpt = 0
    cpt_m = 0
    n = 4 # hauteur de la pyramide
    p = [[randint(0,30) for i in range(j)] for j in range(1,n+1)]
    #p_g = sous_pyramide_gauche(p)
    #p_d = sous_pyramide_droite(p)
    s = somme_pyramide(p)
    s_m = somme_pyramide_mem(p)
    #chemin = parcours_max_pyramide(p)