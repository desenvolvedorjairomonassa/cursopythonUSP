l = int(input("digite a largura:"))
a = int(input("digite a altura:"))

i = 1 #altura
j = 1 #largura
while a >= i:
    while l>=j:
        if j in [1,l] or i in [1,a]:
            print("#",end="")
        else:
            print(" ",end="")
        j+=1
    print()
    j=1
    i+=1
