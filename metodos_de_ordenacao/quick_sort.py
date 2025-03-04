#inf = limite inferior da sua lista
#sup = limite superior da sua lista
def quicksort(l, inf, sup):

    if inf < sup:

        pos = particao(l, inf, sup)
        quicksort(l, inf, pos-1)
        quicksort(l, pos+1, sup)
    
def particao(l, inf, sup):

    pivot = l[inf]
    i = inf + 1
    j = sup

    while i <= j:

        while i <= j and l[i] <= pivot:

            i += 1

        while j >= i and l[j] > pivot:

            j -= 1
        
        if i < j: 

            l[i], l[j] = l[j], l[i]

    
    l[inf], l[j] = l[j], l[inf]

    return j

