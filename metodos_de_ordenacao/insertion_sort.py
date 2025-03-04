def insertionsort(l):

    for i in range(1, len(l)):

        elem = l[i]
        pos = i - 1

        while pos >= 0 and l[pos] > elem:

            l[pos+1] = l[pos]
            pos = pos - 1
            
        l[pos+1] = elem

    return l

