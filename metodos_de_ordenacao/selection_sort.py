def selectionsort(l):

    for pos in range(len(l)):

        menor = pos
        for i in range(pos, len(l)):

            if l[i] <= l[menor]:

                menor = i

        l[pos], l[menor] = l[menor], l[pos]

    return l