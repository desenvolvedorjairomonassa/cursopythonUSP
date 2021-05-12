def menor_nome(nomes):
    ''' busca o menor nome'''
    menor_nome = nomes[0].strip()
    for non in range(1,len(nomes)):
        if len(menor_nome) > len(nomes[non].strip()):
            menor_nome = nomes[non].strip()
    return menor_nome.capitalize()
            

def test_meno():
    m = menor_nome(['maria', 'josé', 'PAULO', 'Catarina'])
    print(m)
    # deve devolver 'José'

    m = menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  '])
    print(m)
    # deve devolver 'José'

    menor_nome(['Bárbara', 'JOSÉ  ', 'Bill'])
    print(m)
    # deve devolver José    
