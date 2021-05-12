def maximo (x,y,z): 
    if x>=y:
        if x>= z:
            return x
        else:
            return z
    else:
        if y>= z:
            return y
        else:
            return z

def test_maximo():
    assert maximo(30,14,10)  == 30

def testmaximo2 ():
    assert maximo(0,-1, 1) == 1    
