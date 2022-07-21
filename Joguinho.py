começo = str(input('você está pronto?'))
nome_jogo = "Jogo da adivinhação"
if começo == 'sim' or começo == 'sim!' or começo == 'pronto' or começo == 'pronto!':
    print(44 * '=')
    print('{:=^44}'.format(nome_jogo))
    print(44 * '=' )

    print('OBJETIVO: Advinhar a palavara misteriosa!!!\n1.Inicialmente,escolha uma letra\n2.Caso a palavra contenha esta letra, será mostrado em que posição(ões) ela se encontra\n3.Entretanto, caso esta letra não exista na palavra,você irá sugerir outra letra\nVAMOS COMEÇAR???\n')

    print(30 * '-')
    print('A PALAVRA MISTERIOSA É ****')

    palavra_misteriosa = ['p','a','t','o']
    letras_contidas = []
    for c in range(0, len(palavra_misteriosa)) :
        letras_contidas.append('*')

    acertou = False

    while acertou == False:
        letra = str(input('Qual letra você acha que contém na palavra? '))
        if len(letra) != 1:
            print('digite apenas uma letra!!!')
        for i in range(0, len(palavra_misteriosa)):
            if letra == palavra_misteriosa[i]:
                letras_contidas[i] = letra
            print(letras_contidas[i])
        acertou = True
        for x in range(0,len(letras_contidas)):
            if letras_contidas[x] != '*':
                continue
            acertou = False

    print('Parabéns,você adivinhou a palavra misteriosa!!!Fim de jogo!!!')
else:
    print('Poxa,que pena...Fica para a próxima!')
