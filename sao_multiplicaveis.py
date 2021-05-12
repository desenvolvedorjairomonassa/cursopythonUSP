def sao_multiplicaveis(m1, m2):
    '''verifica se as matrizes são multiplicaveis
    se o numero de colunas é igual ao numero de linhas da m2'''
    coluna = len(m1[0])
    linha = len(m2)
    return coluna == linha

def test_multi():
    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = [[2, 3, 4], [5, 6, 7]]
    assert sao_multiplicaveis(m1, m2) == False

    m1 = [[1], [2], [3]]
    m2 = [[1, 2, 3]]
    assert sao_multiplicaveis(m1, m2) == True
