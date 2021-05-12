def soma_lista(lista):
    tam = len(lista)
    if tam == 0:
        return 0
    else:
        return lista[-1] + soma_lista(lista[0:tam-1])

def test_soma():
    assert soma_lista([0]) == 0
    assert soma_lista([0,1,2,3]) == 6
    assert soma_lista([-1,-2,3]) == 0
    assert soma_lista([99,100,101]) == 300
