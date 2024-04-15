unites = [20,10,5,2]

def rendu_monnaie(somme_a_rendre):
    nb_pieces = 0
    for p in unites:
        while somme_a_rendre-p >= 0:
            somme_a_rendre -= p
            nb_pieces += 1
    return nb_pieces

def rendu_monnaie_recursif(somme_a_rendre):
    if somme_a_rendre==0:
        return 0
    for p in unites:
        if somme_a_rendre-p >= 0:
            return 1+rendu_monnaie_recursif(somme_a_rendre-p)
        
def rendu_monnaie_rec(somme_a_rendre):
    if somme_a_rendre == 0:
        return 0
    else:
        mini = 1000
    for i in range(len(unites)):
        if unites[i] <= somme_a_rendre:
            nb = 1 + rendu_monnaie_rec(somme_a_rendre-unites[i])
            if nb < mini:
                mini = nb
    return mini