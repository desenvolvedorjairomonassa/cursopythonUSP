num = int(input("Digite um número inteiro:"))
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
if div == 2:
    print("não primo")
else:
    print("primo")
