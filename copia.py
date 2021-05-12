import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a
     ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas
     dentro do texto'''
    sentencas = texto.split(r'[.!?]+')
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_palavras(texto):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro
     da frase'''
    palavras = []
    palavras = texto.split(" ")
    return palavras

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def retirando_pontos(palavra):
    palavra = palavra.replace(".","")
    palavra = palavra.replace(",","")
    palavra = palavra.replace(":","")
    palavra = palavra.replace("!","")
    palavra = palavra.replace("?","")
    return palavra

def tam_medio (lista):
    ''' Tamanho médio de palavra é a soma dos
    tamanhos das palavras dividida pelo número total de palavras.'''
    soma_tam = 0
    quant_palav = 0
    for palav in lista:
        #retirando_pontos(palav)
        tam = len(palav)
        soma_tam = tam+soma_tam
        quant_palav+= 1
    return soma_tam/ quant_palav

def type_token (lista_palavras):
    '''Relação Type-Token é o número de palavras
     diferentes dividido pelo número total de palavras. '''
    quant = 0
    lista2 = []
    total = 0
    j = 0 
    for palav in lista_palavras:
        retirando_pontos(palav)
        palav = palav.lower()
        if palav not in lista2:
            j +=1
            lista2.append(palav)
        total +=1
    return(j/total)

def hapax_legomana (lista):
    '''Razão Hapax Legomana é o
     número de palavras que aparecem uma única vez
     dividido pelo total de palavras.'''
    lista2 = []
    list_rep = []
    total = 0
    j = 0
    #retirar os repetidos , menos o primeiro que aparece
    for palav in lista:
        retirando_pontos(palav)
        palav = palav.lower()
        if palav not in lista2:
            lista2.append(palav)
        else:
            list_rep.append(palav)    
        total +=1
    if list_rep != []:
        for palav in list_rep:
            if palav in lista2:
                lista2.remove(palav)    
    j = len(lista2)
    return(j/total)

def tam_med_sentenca(lista_sentenca):
  '''Tamanho médio de sentença é a soma dos números de
   caracteres em todas as sentenças dividida pelo número de sentenças'''
  soma = 0 
  for palav in lista_sentenca:
    soma += len(palav)
  return (soma / len(lista_sentenca))

def complexidade_sentenca(sentenca, frase):
  '''Complexidade de sentença é o número total
  de frases divido pelo número de sentenças.'''
  f = len(frase)
  s = len(sentenca)
  if s > 0 and f > 0:
    return f/s
  else:
    return 0
def tam_medio_frase(frase):
    '''Tamanho médio de frase é a soma do número
    de caracteres em cada frase dividida pelo número de frases no texto'''
    if frase != []:
        soma = 0
        for palav in frase:
            soma += len(palav)
        return soma / len(frase)

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e
    deve devolver o grau de similaridade nas assinaturas.'''
    soma = 0
    for i in range (0,6,1):
      soma += abs(as_a[i] - as_b[i])
    #print (soma)
    return soma/6

def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    palavras = separa_palavras(texto)
    sentencas = separa_sentencas(texto)
    frases = separa_frases(texto)
    wal = tam_medio(palavras)
    ttr = type_token(palavras)
    hlr = hapax_legomana(palavras)
    sal = tam_med_sentenca(sentencas)
    sac = complexidade_sentenca(sentencas,frases)
    pal = tam_medio_frase(frases)
    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    ''' Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n)
    do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    ass_txt = []
    list_sim = []
    for text in textos:
      ass_txt = calcula_assinatura(text)
      sim = compara_assinatura(ass_cp, ass_txt)
      list_sim.append(sim)
    sim = list_sim[0]
    menor = 1 #considerando o menor texto o primeiro
    for i  in range(1,len(list_sim)):
      if list_sim[i] < sim:
        sim = list_sim[i]
        menor = i
    return menor
  
def teste_sentenca():
    sep = separa_sentencas("o gato caçou o rato. velho rato que não correu")
    assert len(sep) == 2

def teste_type ():
    assert type_token(["o","gato","caça","o", "rato"]) == 0.8
    assert type_token(["o","gato","caça","O", "rato"]) == 0.8
def teste_hapax ():
    assert hapax_legomana(["o","gato","caça","o", "rato"]) == 0.6
    assert hapax_legomana(["o","gato","caça","O", "rato"]) == 0.6
    assert hapax_legomana(["o","gato","caça","O", "rato","o"]) == 0.5

def teste_tam_med_sent ():
    sep = separa_sentencas("o gato caçou o rato. velho rato que não correu")
    assert tam_med_sentenca(sep) == 22.5
def test_tamanho ():
  texto1 = "Navegadores antigos tinham uma frase gloriosa:"'Navegar é preciso; viver não é preciso'".Quero para mim o espírito [d]esta frase,transformada a forma para a casar como eu sou:Viver não é necessário; o que é necessário é criar.Não conto gozar a minha vida; nem em gozá-la penso.Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo.Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha.Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça."
  texto2 = "Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres."
  texto3 = "NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência."
  lista_palavras = []
  assert tam_medio(separa_palavras(texto3)) == 5.324324324324325
  assert tam_medio(separa_palavras(texto2)) == 4.73015873015873
  assert tam_medio(separa_palavras(texto1)) == 5.008695652173913
  print(tam_medio(separa_palavras(texto1)))
  
def main ():
  textos = []
  ass_principal = le_assinatura()
  textos = le_textos()
  menor_texto = avalia_textos(textos,ass_principal)
  return print("O autor do texto", menor_texto, "está infectado com COH-PIAH.")

def test_main ():
  '''testes do programa principal'''
  textos = []
  texto1 = "Navegadores antigos tinham uma frase gloriosa: Navegar é preciso; viver não é preciso. Quero para mim o espírito [d]esta frase, transformada a forma para a casar como eu sou: Viver não é necessário; o que é necessário é criar. Não conto gozar a minha vida; nem em gozá-la penso. Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo. Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha. Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça."
  texto2 = "Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres."
  texto3 = "NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência."
  assi_principal = [4.79, 0.72, 0.56, 80.5, 2.5, 31.6]
  textos.append(texto1)
  textos.append(texto2)
  textos.append(texto3)
  print (assi_principal)
  print(textos)
  print(calcula_assinatura(texto1))
  menor_texto = avalia_textos(textos, assi_principal)
  print(menor_texto)
  
  

