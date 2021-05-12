
lista = []
n = int(input("Digite um número:"))
while n != 0:
    lista.append(n)
    n = int(input("Digite um número:"))
#inverter lista
for j in range(len(lista)-1,-1,-1):
    print (lista[j])
    

    
