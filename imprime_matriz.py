def imprime_matriz(matriz):
    ''' imprime matriz'''
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if j != len(matriz[0])-1:
                print(matriz[i][j],end=' ')
            else:
                print(matriz[i][j])
        #print('',end='\n')

def test_imp_m():
    ''' teste da imprime matriz'''
    minha_matriz = [[1], [2], [3]]
    imprime_matriz(minha_matriz)
    minha_matriz = [[1, 2, 3], [4, 5, 6]]
    imprime_matriz(minha_matriz)
