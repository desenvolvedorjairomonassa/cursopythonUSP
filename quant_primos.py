def primo(num):
    i = 1
    div = 0
    while (num != i):
        if num%i ==  0:
            div+=1
            i+=1
            if div == 2:
                break;
        else:
            i+=1
    return div != 2
def n_primos(num):
    j = 2
    contar = 0
    while num >= j:
        if primo(j):
            contar+=1
        j+=1
    return contar
