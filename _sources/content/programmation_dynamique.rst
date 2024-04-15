La programmation dynamique
==========================

.. admonition:: Définition
    :class: definition

    On peut dire que la résolution algorithmique d'un problème relève de la programmation dynamique si:

    -   le problème peut être résolu à partir de sous-problèmes similaires mais plus petits ;
    -   on peut les indexer et ranger les résultats des sous-problèmes dans un tableau ;
    -   la solution optimale au problème posé s’obtient à partir des solutions optimales des sous-problèmes ;
    -   les sous-problèmes ne sont pas indépendants et un traitement récursif fait apparaître les mêmes sous-problèmes un grand nombre de fois.

On souhaite relier 2 points d'une grille composée de trois lignes et colonnes en se déplaçant uniquement horizontalement à droite et verticalement vers le bas.

.. figure:: ../img/grille_3x4.svg
    :align: center

#.  La détermination du nombre de chemin se décompose en sous-problèmes similaires avec des grilles plus petites;

    ..  figure:: ../img/nombre_chemins.svg
        :align: center

#.  La fonction qui résout chaque problème est la même en ajustant les dimensions de la grille. C'est donc une fonction récursive. On peut visualiser les différents appels ci-dessous en remarquant que certains appels se répètent.

    .. figure:: ../img/appels_recursifs_nombre_chemins.svg
        :align: center

#.  Une fois résolu, le résultat de chaque sous-problème est mémorisé dans un tableau. À chaque appel récursif, on vérifie si la valeur a déjà été calculée et mémorisée.

    .. code:: python
        
        mem = [
            [nombre_chemins(1,1),nombre_chemins(1,2),nombre_chemins(1,3),nombre_chemins(1,4)],
            [nombre_chemins(2,1),nombre_chemins(2,2),nombre_chemins(2,3),nombre_chemins(2,4)],
            [nombre_chemins(3,1),nombre_chemins(3,2),nombre_chemins(3,3),nombre_chemins(3,4)],
        ]

#.  La solution du problème initial s'obtient par addition des valeurs de chaque sous-problème;



