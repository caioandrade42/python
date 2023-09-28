from os import system
from random import choice

animais = [
    "cachorro", "gato", "elefante", "leao", "tigre", "urso", "macaco", "panda",
    "girafa", "zebra", "cavalo", "vaca", "porco", "ovelha", "galinha", "pato",
    "passaro", "peixe", "tartaruga", "coelho"
]

frutas = [
    "maca", "banana", "laranja", "uva", "manga", "abacaxi", "melancia",
    "morango", "kiwi", "limao", "pessego", "cereja", "amora", "caju", "goiaba",
    "acerola", "maracuja", "coco", "abacate", "melao"
]

partes_corpo = ["o", "|", "/", "\\"]

MAX_TENTATIVAS = 6


class Forca():
    def __init__(self) -> None:
        self.resetar()

    def resetar(self) -> None:
        self.__tentativa = 0
        self.__palavra = []
        self.__letras_utilizadas = set()
        self.__dicionario = {}
        self.__corpo = [" ", " ", " ", " ", " ", " "]

    def jogar(self) -> None:
        palavra_sorteada = self.__sortear_palavra()
        self.__palavra = ['_' for _ in palavra_sorteada]

        if (palavra_sorteada is None):
            return

        self.__cria_dicionario(palavra_sorteada)

        while True:
            system("cls")
            print("{:^24}".format(", ".join(self.__letras_utilizadas)))
            print("{:^24}".format(''.join(self.__palavra)))
            self.__imprime_corpo()
            chute = input("Digite uma letra: ")
            self.__fazer_tentativa(chute)

            if self.__tentativa == MAX_TENTATIVAS and len(self.__dicionario):
                system("cls")
                self.__imprime_corpo()
                print("Você perdeu ;-;")
                print("A palavra era", palavra_sorteada)
                break
            elif not len(self.__dicionario):
                system("cls")
                self.__imprime_corpo()
                print("Parabéns, a palavra é", palavra_sorteada)
                break

    def __sortear_palavra(self) -> str | None:
        while True:
            print("1 - Animais")
            print("2 - Frutas")
            print("3 - Sair")
            opcao = (int)(input())
            system("cls")
            if opcao == 1:
                return choice(animais)
            elif opcao == 2:
                return choice(frutas)
            elif opcao == 3:
                return

    def __cria_dicionario(self, palavra: str) -> None:
        self.__dicionario = {}
        for i in range(len(palavra)):
            self.__dicionario.setdefault(palavra[i], []).append(i)

    def __fazer_tentativa(self, chute: chr) -> None:
        if not str.isalpha(chute):
            return
        if chute in self.__dicionario:
            for i in self.__dicionario[chute]:
                self.__palavra[i] = chute
            self.__dicionario.pop(chute)
        elif chute not in self.__letras_utilizadas:
            self.__tentativa += 1

        self.__letras_utilizadas.add(chute)

    def __imprime_corpo(self) -> None:
        if self.__tentativa == 1:
            self.__corpo[0] = partes_corpo[0]
        elif self.__tentativa == 2:
            self.__corpo[1] = partes_corpo[1]
        elif self.__tentativa == 3:
            self.__corpo[2] = partes_corpo[2]
        elif self.__tentativa == 4:
            self.__corpo[3] = partes_corpo[3]
        elif self.__tentativa == 5:
            self.__corpo[4] = partes_corpo[2]
        elif self.__tentativa == 6:
            self.__corpo[5] = partes_corpo[3]

        print("\t _______")
        print("\t/       \\")
        print("\t|       |")
        print(f"\t|       {self.__corpo[0]}")
        print(f"\t|      {self.__corpo[2]}{self.__corpo[1]}{self.__corpo[3]}")
        print(f"\t|      {self.__corpo[4]} {self.__corpo[5]}")
        print()