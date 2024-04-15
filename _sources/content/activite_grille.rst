Parcourir une grille
=====================

.. rubric:: Le problème

La grille ci-dessous est formée par des carrés. Elle contient 3 lignes et 4 colonnes. On place au sommet haut à gauche un départ et une arrivée au sommet en bas à doite.

.. figure:: ../img/grille_3x4.svg
    :align: center

On se déplace en suivant la grille. Les déplacements autorisés sont :

-  soit horizontalement vers la droite et pas à gauche;
-  soit verticalement vers le bas et pas en haut.

Combien existe-t-il de chemins différents pour cette grille pour relier le départ à l'arrivée ?

.. rubric:: Recherche de stratégie

#.  Le problème peut se décomposer en 2 sous-problèmes avec des grilles plus petites. Quelle est cette décomposition et comment sont les grilles ?
#.  Chaque sous-problème peut se décomposer en problèmes avec des grilles petites ou jusqu'à un cas de base dont le nombre de chemins est invariablement le même. Quel est ce cas de base ?
#.  Regrouper dans un même arbre toute la décomposition du problème jusqu'aux cas de base. En déduire la solution du problème.
#.  Le problème précédent est lui même un sous-problème d'un problème avec une grille plus grande. Quel est ce problème et comment déterminer le nombre de chemins ?

.. rubric:: Cas général

Comment déterminer le nombre de chemins pour une grille ``g(n,p)`` contenant ``n`` lignes et ``p`` colonnes ?

#.  Lorsqu'on effectue un déplacement vers le bas, quel parmètre est modifié ? Et vers la droite ?
#.  Quelles sont les valeurs possibles pour ``n`` et ``p`` ?
#.  Que se passe-t-il lorsque ``n = 1`` ou ``p = 1`` ?
#.  Comment peut-on décomposer le problème avec une grille ``g(n,p)`` en 2 sous-problèmes ?

.. rubric:: Programmation python

La fonction ``nombre_chemins`` a pour paramètres deux nombres entiers ``n`` et ``p`` représentant la grille. Elle renvoie le nombre de chemins pour relier le départ à l'arrivée.

#.  D'après l'analyse précédente, est-il préférable de programmer une fonction **itérative** ou **récursive** pour calculer le nombre de chemins dans une grille ``g(n,p)``.
#.  Écrire la fonction en Python et vérifier que celle-ci renvoie le bon nombre de chemins pour une grille ``(3,4)``.
#.  Ajouter des **préconditions** avec ``assert`` sur les paramètres ``n`` et ``p`` pour vérifier leurs valeurs.
#.  Combien d'appels récursifs sont nécessaires pour calculer le nombre de chemins dans une grille ``(3,4)``. De même pour une grille ``(5,7)``.

.. rubric:: Programmation dynamique

On remarque que certains appels récursifs se font avec les mêmes paramètres, et ça plusieurs fois.

#.  Dans le cas de la grille ``(3,4)`` quels sont les appels récursifs qui se répètent et combien de fois ?
#.  Comment éviter tous ces appels récursifs qui se répètent ?
#.  Modifier le code en Python de la fonction précédente pour éviter les appels récursifs.
#.  Combien d'appels récursifs sont nécessaires pour calculer le nombre de chemins dans une grille ``(3,4)``. De même pour une grille ``(5,7)``.
