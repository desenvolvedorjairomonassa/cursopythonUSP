def maior_elemento (lista):
    maior = lista[0]
    for x in lista:
        if x > maior:
            maior = x
    return maior

def test_maior ():
    lista = [1,20,3,50]
    assert maior_elemento(lista) == 50
