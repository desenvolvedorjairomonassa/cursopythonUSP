def incomodam(n):
    if n <= 0:
        return ''
    else:
        return 'incomodam '+ incomodam (n-1)
    
def elefantes (n):
    if n<=1:
        return ''
    elif n == 2:
        print('Um elefante incomoda muita gente')
        print(str(n) + ' elefantes ' + incomodam(n) + 'muito mais')
        print (str(n) + ' elefantes ' + incomodam(n) + 'muita gente')        
    else:
        elefantes(n-1)
        print(str(n) + ' elefantes ' + incomodam(n) + 'muito mais')
        print (str(n) + ' elefantes ' + incomodam(n) + 'muita gente')
        
