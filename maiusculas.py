def maiusculas(frase):
    '''recebe uma frase e devolve outra frase com as
    letras maiusculas somente'''
    novafrase = ''
    for i in range(len(frase)):
        if 64 < ord(frase[i]) < 91:
            novafrase = novafrase + frase[i]
    return (novafrase)

def test_mai():
    maiusculas('Programamos em python 2?')
    # deve devolver 'P'

    maiusculas('Programamos em Python 3.')
    # deve devolver 'PP'

    maiusculas('PrOgRaMaMoS em python!')
    # deve devolver 'PORMMS'    
