def primo(num):
    i = 1
    div = 0
    while (num != i):
        if num%i ==  0:
            div+=1
            i+=1
            if div == 2:
                break;
        else:
            i+=1
    return div != 2
def primo_div3_resto1(num):
    return (primo(num) and (num%4 == 1))
def e_hipotenusa (num):
    i = 2
    achou= False
    while num >= i:
        if primo_div3_resto1(i) and num%i == 0:
            achou=True
            break
        i+=1
    #print(achou)
    return achou
def soma_hipotenusas(num):
    j=1
    soma=0
    while num>=j:
        if e_hipotenusa(j):
            soma=soma+j
        j+=1
    return soma

#z ´e divis´ıvel por um numer ´ o primo p tal que p ≡ 1 (mod 4),
#i. e. p deixa resto 1 quando dividido por 4.

