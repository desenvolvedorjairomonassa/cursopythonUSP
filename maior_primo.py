def eprimo (num):
    i = 2
    outrodivisor = False
    while (num != i) and num != 1 and not outrodivisor:
        outrodivisor = num%i == 0            
        i+=1
    return outrodivisor == False

def maior_primo (num) :
    achouprimo = False
    while num != 2 and not achouprimo:
        achouprimo = (eprimo (num))
        if not achouprimo:
            num-=1
    return num

def test_marior_primo100 ():
    assert maior_primo(100) == 97

def test_maior_primo7 ():
    assert maior_primo(7) == 7
    
