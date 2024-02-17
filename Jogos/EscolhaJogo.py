import JogoAdivinhacao
import JogoForca

def escolha_jogo():
    print("Bem-vindo ao menu incial!")

    print("Por favor, escolha seu jogo:")

    forca = 1
    adivinhacao = 2

    jogo = int(input("(1) Forca (2) Adivinhação - Informe apenas o número: "))

    print("Jogo selecionado foi: {}".format(jogo))

    if (jogo == 1):
        print("Jogo da forca:")
        JogoForca.jogar()
    elif (jogo == 2):
        print("Jogo adivinhação:")
        JogoAdivinhacao.jogar()

    else:
        print("O número selecionado não corresponde aos jogos disponíveis")


if (__name__ == "__main__"):
    escolha_jogo()
