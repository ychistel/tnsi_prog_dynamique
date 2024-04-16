def rendu_monnaie(somme_a_rendre):
    unites = [50,20,10,5,2,1]
    n = 0
    for p in unites:
        while somme_a_rendre-p >= 0:
            somme_a_rendre -= p
            n = n + 1
    return n

