import random

def jogar():

    mensagemInicial()

    PalavraSecreta = selecaoPalavraSecreta()

    letras_acertadas = acertos(PalavraSecreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):
        chute = tentativa()

        if (chute in PalavraSecreta):
            tentativaCorreta(chute, letras_acertadas, PalavraSecreta)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(PalavraSecreta)

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(PalavraSecreta):
    print ("Puxa, você foi enforcado!")
    print ("A palavra era {}".format(PalavraSecreta))
    print ("    _______________         ")
    print ("   /               \       ")
    print ("  /                 \      ")
    print ("//                   \/\  ")
    print ("\|   XXXX     XXXX   | /   ")
    print (" |   XXXX     XXXX   |/     ")
    print (" |   XXX       XXX   |      ")
    print (" |                   |      ")
    print (" \__      XXX      __/     ")
    print ("   |\     XXX     /|       ")
    print ("   | |           | |        ")
    print ("   | I I I I I I I |        ")
    print ("   |  I I I I I I  |        ")
    print ("   \_             _/       ")
    print ("     \_         _/         ")
    print ("       \_______/           ")


def mensagemInicial():
    print("********************************")
    print("Seja bem-vindo ao jogo da forca!")
    print("********************************")


def selecaoPalavraSecreta():
    arquivo = open(
        '/Users/frois/Library/CloudStorage/GoogleDrive-juan.frois9@gmail.com/Meu Drive/Estudos/JuanFrois/Cursos/Alura/BackEnd/Python/CriandoJogos/Jogos/PalavrasSecretas.txt',
        "r")
    Palavra = []
    for linha in arquivo:
        linha = linha.strip()
        Palavra.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(Palavra))
    PalavraSecreta = Palavra[numero].upper()
    return PalavraSecreta

def acertos(Palavra):
    return ["_" for letra in Palavra]


def tentativa():
    chute = input("Informe a letra que gostaria de jogar:")
    chute = chute.strip().upper()
    return chute



def tentativaCorreta(chute, letras_acertadas, PalavraSecreta):
    index = 0
    for letra in PalavraSecreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1




if (__name__ == "__main__"):
    jogar()
