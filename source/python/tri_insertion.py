def tri(t):
    for i in range(1,len(t)):
        j=i
        m = t[j]
        while j > 0 and t[j-1] > m:
            t[j] = t[j-1]
            j = j-1
        t[j] = m
    return t

t = tri([9,2,6,1,5,3])