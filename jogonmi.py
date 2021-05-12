    
def computador_escolhe_jogada (n, m):
    #restam
    num  = 1
    while ((n-num)%(m+1) !=0) and (num !=m):
        num +=1
    if num == 1:        
        print("O computador tirou uma peça.")
    else:
        print("O computador tirou", num, "peças." )    
    return num

def usuario_escolhe_jogada (n,m):
    num=0
    #tenho que retirar pelo menos uma peça
    #não pode retirar um valor maior ue o maximo
    #não pode retirar mais peças que existem
    while (num <= 0) or (num > m) or (num > n):
        num = int(input("Quantas peças você vai tirar?"))
        if (num > m) or (num <= 0 ) or (num >n):
            print("Oops! Jogada inválida! Tente de novo.")
    if num == 1:        
        print("Você tirou uma peça.")
    elif num >= 1:
        print("Você tirou", num, "peças." )
    return num    

def partida():
    n = int(input("Quantas peças?"))
    m = int(input("Limite de peças por jogada?"))
    resto = n
    vez_computador = True
    if n%(m+1) == 0:
        print("Voce começa!")
        vez_computador = False
    else:
        print("Computador começa!")

    while resto !=0:
        if vez_computador:
            num = computador_escolhe_jogada(resto,m)
        else:
            num = usuario_escolhe_jogada(resto,m)
        #peças restantes
        resto = resto-num
        if resto == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
        elif resto > 1:
            print("Agora resta apenas", resto,"peças no tabuleiro.")
        vez_computador = not vez_computador
    if not vez_computador:
        print("Fim do jogo! O computador ganhou!")
        return "Computador"
    else:
        print ("Fim do jogo! Você ganhou!") #nunca vai acontecer
        return "Usuário"

def campeonato():
    j = 1
    comp = 0
    usu = 0 
    while j <=3:
        print("**** Rodada ", j, "****")
        if partida() == "Computador":
            comp +=1
        else:
            usu +=1
        j += 1
    print("**** Final do campeonato! ****")
    print("Placar: Você", usu,"X",comp,"Computador")
    
print("Bem-vindo ao jogo do NIM!:")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato 2")
n = 4
while not n in [0,1,2]:
    n = int(input("Escolha:"))
if n == 1:
    print("Voce escolheu uma partida isolada!")
    partida()
elif n == 2:
    print ("Voce escolheu um campeonato!")
    campeonato()

        
