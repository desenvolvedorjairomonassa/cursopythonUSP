l = int(input("digite a largura:"))
a = int(input("digite a altura:"))

i = 1
j = 1
while a >= i:
    while l>=j:
        print("#",end="")
        j+=1
    print()
    j=1
    i+=1
