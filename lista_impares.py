def  encontra_impares(lista):
    ''' Encontrando ímpares em uma lista'''
    tam = len(lista)
    #print(lista)
    if tam == 0:
        return []
    listaimpar = lista[1:tam]
    if lista[0] % 2 != 0:
        return [lista[0]] + encontra_impares(listaimpar)
    return encontra_impares(listaimpar)

    
a = [1,2,3,4,5,6,7]
c = encontra_impares(a)
print(c)
