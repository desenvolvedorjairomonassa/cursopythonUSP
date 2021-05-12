import math
numx1 = int(input("Digite o primeiro:"))
numy1 = int(input("Digite o segundo:"))
numx2 = int(input("Digite o terceiro:"))
numy2 = int(input("Digite o quarto:"))
                  
distancia12 = math.sqrt((numx2-numx1)**2 + (numy2-numy1)**2)
if distancia12 >= 10:
    print("longe")
else:
    print("perto")
