from os import system
from forca import Forca

OPCAO_SAIDA = 2


def main():
    menu()


def menu() -> None:
    forca = Forca()
    while True:
        print("{:-^30}".format("Jogo da Forca"))
        print("1 - Jogar")
        print("2 - Sair")
        opcao = (int)(input())
        system('cls')
        if opcao == 1:
            forca.jogar()
        elif opcao == OPCAO_SAIDA:
            break


if __name__ == "__main__":
    main()