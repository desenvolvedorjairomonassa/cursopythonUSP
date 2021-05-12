num = int(input("Digite um número inteiro:"))

encontrado = False
digant = num%10
num = num//10
while num != 0 and not encontrado:
    dig = num%10
    encontrado = dig == digant
    digant = dig
    num = num//10
if encontrado:
    print ("sim")
else:
    print("não")
        
