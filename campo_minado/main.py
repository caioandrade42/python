from os import system
from campo_minado import CampoMinado

OPCAO_SAIDA = 2


def main() -> None:
    menu()


def menu() -> None:
    campo_minado = CampoMinado(10, 10)
    while True:
        print("{:-^30}".format("Campo Minado"))
        print("1 - Jogar")
        print("2 - Sair")
        opcao = (int)(input())
        system('cls')
        if opcao == 1:
            campo_minado.play()
        elif opcao == OPCAO_SAIDA:
            break


if __name__ == "__main__":
    main()