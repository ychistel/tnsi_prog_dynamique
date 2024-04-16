def recherche(t,v):
    a = 0
    b = len(t)-1
    m = (a+b)//2
    while a <= b:
        if v < t[m]:
            b = ...
        elif v > t[m]:
            a = ...
        else:
            return m
        m = (a+b)//2

        
t = [3,7,8,11,14,16,17,19,22,23,25,29,32]
position = recherche(t,11)