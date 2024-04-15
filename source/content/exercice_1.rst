Exercices
=========

Exercice 1
------------

La suite de Fibonnacci est une suite de nombres où chaque nombre (en dehors des 2 premiers) est obtenu par l'addition des 2 nombres qui le précèdent.

Par exemple, en prenant comme nombres initiaux ``0`` et ``1``, on déduit la suite des nombres: ``0,1,1,2,3,5,8,13,...``. Pour identifier chaque nombre de la suite, on les note de la façon suivante:

.. code:: python

    fibo(0) = 0
    fibo(1) = 1
    fibo(2) = fibo(0) + fibo(1) = 1
    fibo(3) = fibo(1) + fibo(2) = 2
    etc.

On se propose d'écrire une fonction récursive pour calculer un terme de la suite de Fibonnacci. On donnera ensuite une version en programmation dynamique.

#.  Calculer ``fibo(8)``.
#.  Écrire en Python la fonction récursive ``fibo`` qui prend en paramètre un nombre entier et renvoie le terme de la suite de Fibonnacci qui lui est associé.
#.  Représenter par un arbre les différents appels récursifs du calcul de ``fibo(8)``.
#.  Certains appels récursifs apparaissent à plusieurs reprises. Ajouter dans votre une fonction un tableau qui mémorise les valeurs calculées pour éviter un appel récursif.

Exercice 2
-----------

Le problème du rendu de monnaie consiste à réaliser une somme en utilisant le moins de pièces et billets possible. On admet que l'on dispose de pièces de 1 et 2 euros ainsi que de billets de 5, 10 et 20 euros en nombre illimité.

#.  On propose une première fonction ``rendu_monnaie`` qui résout le problème.

    .. code:: Python

        unites = [20,10,5,2,1]

        def rendu_monnaie(somme_a_rendre):
            nb_pieces = 0
            for p in unites:
                while somme_a_rendre-p >= 0:
                    somme_a_rendre -= p
                    nb_pieces += 1
            return nb_pieces

    a.  Quel est l'algorithme utilisé par cette fonction ?
    b.  Quel avantage et inconvénient a-t-on avec cet algorithme ?

#.  On propose une version récursive incomplète de la fonction précédente:

    .. code:: python

        unites = [20,10,5,2,1]

        def rendu_monnaie_recursif(somme_a_rendre):
            if somme_a_rendre == 0:
                return ...
            for p in unites:
                if somme_a_rendre-p >= 0:
                    return 1 + rendu_monnaie_recursif(...)

    a.  Compléter le code de la fonction récursive.
    b.  On effectue en console l'appel ``rendu_monnaie_recursif(34)``. Donner les différents appels récursifs.

#.  Dans cette question et les suivantes, on admet que l'on dispose de pièces de 2 euros et de billets de 5, 10 et 20 euros. 
    a.  Quelle conséquence cela a-t-il de ne plus avoir de pièces de 1 euro ?
    b.  On rend la monnaie sur 11 euros avec les fonctions précédentes. Que remarque-t-on ? 
#.  Comme on vient de le voir, l'agorithme glouton ne trouve pas de solution pour rendre 11 euros mais pourtant une solution existe bien ! On peut décomposer le problème de rendu de monnaie en sous-problèmes de même nature. Pour rendre la somme de 11 euros, cela revient à rendre 1 unité parmi ``[20,10,5,2]`` puis à rendre une somme réduite de cette unité. 
    a.  Quelles ont les unités que l'on peut rendre sur 11 euros et quelles sont alors les sommes à rendre ?
    b.  Représenter par un arbre toutes les possibilités pour rendre 11 euros.

#.  On propose le code en Python suivant:

    .. code:: python

        