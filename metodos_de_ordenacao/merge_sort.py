def mergesort(lista):

    if len(lista) > 1:

        meio = len(lista)// 2

        lesq = lista[:meio]
        ldir = lista[meio:]

        mergesort(lesq)
        mergesort(ldir)

        merge(lista, lesq, ldir)

def merge(lista, lesq, ldir):

    i = 0
    j = 0
    k = 0

    while len(lesq) > i and len(ldir) > j:

        if lesq[i] < ldir[j]:

            lista[k] = lesq[i]

            i += 1

        else:

            lista[k] = ldir[j]
            j += 1

        k += 1

    while len(lesq) > i:

        lista[k] = lesq[i]

        i += 1
        k += 1

    while len(ldir) > j:

        lista[k] = ldir[j]

        j += 1
        k += 1

    return lista


