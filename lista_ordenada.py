def ordenada(lista):
    tam = len(lista)
    for i in range(tam):
        for j in range(i+1,tam):
            if lista[i]> lista[j]:
                return False
    return True

        
