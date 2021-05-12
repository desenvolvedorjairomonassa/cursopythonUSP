def dimensoes(matriz):
    ''' mostra tamanho da matriz, formato 3x1'''
    linha = len(matriz)
    if linha > 0:
        coluna = len(matriz[0])
    return str(linha) + 'X' + str(coluna)    
    

def soma_matrizes(m1, m2):
    '''soma das matriz com a linha e coluna'''
    if dimensoes(m1) != dimensoes(m2):
        return False
    else:        
        linha = len(m1)
        if linha > 0:
            coluna = len(m1[0])
        matriz = []
        for i in range(linha):
            m3 = []
            for j in range(coluna):
                soma = int(m1[i][j]) + int(m2[i][j])
                m3.append(soma)
            matriz.append(m3)
        return matriz
        

def test_soma_matriz():
    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = [[2, 3, 4], [5, 6, 7]]
    m3 = soma_matrizes(m1, m2)
    assert m3 == [[3, 5, 7], [9, 11, 13]]
    #print(m3)
    m1 = [[1], [2], [3]]
    m2 = [[2, 3, 4], [5, 6, 7]]
    m3 = soma_matrizes(m1, m2)
    assert  m3 == False
    #print(m3)
