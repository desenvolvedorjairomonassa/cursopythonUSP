import math
numa = float(input("Digite o a:"))
numb = float(input("Digite o b:"))
numc = float(input("Digite o c:"))

delta = numb**2 - (4*numa*numc) 
if delta < 0 :
    print("esta equação não possui raízes reais")
elif delta == 0: 
    raiz =  -numb/2*numa
    print("a raiz desta equação é",raiz) 
else:    
    raiz1 = (-numb - math.sqrt(delta))/(2*numa)
    raiz2 = (-numb + math.sqrt(delta))/(2*numa)
    if raiz1 > raiz2:
        print("as raízes da equação são", raiz2, "e", raiz1)
    else:
        print("as raízes da equação são", raiz1, "e", raiz2)
