def dimensoes(matriz):
    ''' mostra tamanho da matriz, formato 3x1'''
    linha = len(matriz)
    coluna = len(matriz[0])
    dim = str(linha) + 'X' + str(coluna) 
    return print(dim)   
    
def test_tam ():
    minha_matriz = [[1], [2], [3]]
    assert dimensoes(minha_matriz) == '3X1'
    minha_matriz = [[1, 2, 3], [4, 5, 6]]
    assert dimensoes(minha_matriz) == '2X3'
    minha_matriz = [[1, 2], [3, 4]]
    assert dimensoes(minha_matriz) == '2X2'


