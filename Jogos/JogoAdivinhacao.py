import random


def jogar():
    print("******************************************************************************")

    print("Boas vinda ao nosso jogo de adivinhação, aqui você terá uma experiência única)")
    print("******************************************************************************")


    numeroSorteado = random.randrange(1, 101)
    chances = 0
    pontos = 1000

    print("Por favor informe o nível que você gostaria de jogar:")
    print("(1) Fácil (2) Médio (3) Difícil - Basta digitar o número que deseja!")
    nivel = int(input("Informe o nível: "))

    if (nivel == 1):
        chances = 20
    elif (nivel == 2):
        chances = 10
    else:
        chances = 5

    for rodada in range(1, chances + 1):
        print("Tentativa {} de {}".format(rodada, chances))
        tentativa = int(input("Por favor digite seu número entre 1 e 100: "))
        print("Você digitou: ", tentativa)

        if (tentativa < 1 or tentativa > 100):
            print("Você digitou um número diferente do pedido, por favor digite um número entre 1 e 100")
            continue
    
        acertou = tentativa == numeroSorteado
        maior = tentativa > numeroSorteado
        menor = tentativa < numeroSorteado

     
        if (acertou):
            print("Você acertou! Meus parabéns! Você ganhou {} pontos!)".format(pontos))
            break
        else:
            if (maior):
                print("O número digitado foi maior que o número da sorte definido")
            elif (menor):
                print("O número digitado foi menor que o número da sorte definido")

            calculo_pontuacao = abs(numeroSorteado - tentativa)
            pontos = pontos - calculo_pontuacao

    print("Fim do jogo meus queridos!")


if (__name__ == "__main__"):
   jogar()
