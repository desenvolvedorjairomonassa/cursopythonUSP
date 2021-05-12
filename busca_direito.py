numeros = [55,33,0,900,-432,10,77,2,11]
lista = numeros
fim = len(lista)
for i in range(fim-1):
    pos_menor = i
    for j in range(i+1,fim):
        if lista[j] < lista[pos_menor]:
            pos_menor = j
        if lista[j] == 2:
             print('2')
        if lista[pos_menor] == 2:
            print('21')
    lista[i],lista[pos_menor] = lista[pos_menor],lista[i]
print(lista)

