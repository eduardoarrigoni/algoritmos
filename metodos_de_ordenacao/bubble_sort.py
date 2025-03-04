def bubblesort(l):

    for pos in range(len(l)):

        for i in range(len(l) - pos -1):

            if l[i] > l[i+1]:

                troca(l, i, i+1)

            
    return l

def troca(l, x, y):

    aux = l[x]
    l[x] = l[y]
    l[y] = aux

