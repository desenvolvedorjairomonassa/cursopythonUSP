def remove_repetidos(lista):
    list_rem = []
    for ele in lista:
        if ele not in list_rem:
            if list_rem is not []:
                list_rem.append(ele)
    list_rem.sort()
    return list_rem
        
