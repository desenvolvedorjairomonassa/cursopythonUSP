def busca(lista,elemento):
    tam = len(lista)
    for i in range(tam):
        if lista[i] == elemento:
            return i
    return False
