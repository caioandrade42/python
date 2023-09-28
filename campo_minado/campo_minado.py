from os import system
import random

BOMBA = '*'


class CampoMinado():
    def __init__(self, tamanho, num_bombas):
        self.__tamanho = tamanho
        self.__num_bombas = num_bombas
        self.__resetar()

    def __resetar(self) -> None:
        self.__tabuleiro = [[0 for _ in range(self.__tamanho)]
                            for _ in range(self.__tamanho)]
        self.__cavado = set()

    def play(self) -> None:
        self.__resetar()
        self.__iniciar_bombas()
        while len(self.__cavado) < self.__tamanho ** 2 - self.__num_bombas:
            self.__imprimir_tabuleiro()
            linha = (int)(input("Digite a linha: "))
            coluna = (int)(input("Digite a coluna: "))

            if linha < 0 or linha >= self.__tamanho or coluna < 0 or coluna >= self.__tamanho:
                system("cls")
                print("Posição Inválida")
                continue

            seguro = self.__cavar(linha, coluna)

            if not seguro:
                break

        if seguro:
            print("Parabéns, você ganhou")
        else:
            print("Game Over")
            for l in range(self.__tamanho):
                for c in range(self.__tamanho):
                    self.__cavar(l, c)
            self.__imprimir_tabuleiro()

    def __iniciar_bombas(self) -> None:
        bombas_plantadas = 0
        while bombas_plantadas != self.__num_bombas:
            pos = random.randint(0, self.__tamanho ** 2 - 1)
            linha = pos // self.__tamanho
            coluna = pos % self.__tamanho

            if self.__tabuleiro[linha][coluna] == BOMBA:
                continue
            self.__tabuleiro[linha][coluna] = BOMBA
            bombas_plantadas += 1
            self.__marcar_bombas_vizinhas(linha, coluna)

    def __marcar_bombas_vizinhas(self, linha: int, coluna: int) -> None:
        for l in range(max(0, linha - 1), min(self.__tamanho - 1, linha + 1) + 1):
            for c in range(max(0, coluna - 1), min(self.__tamanho - 1, coluna + 1) + 1):
                if l == linha and c == coluna or self.__tabuleiro[l][c] == BOMBA:
                    continue
                self.__tabuleiro[l][c] += 1

    def __cavar(self, linha: int, coluna: int) -> bool:
        self.__cavado.add((linha, coluna))
        if self.__tabuleiro[linha][coluna] == BOMBA:
            return False
        if self.__tabuleiro[linha][coluna] > 0:
            return True

        for l in range(max(0, linha - 1), min(self.__tamanho - 1, linha + 1) + 1):
            for c in range(max(0, coluna - 1), min(self.__tamanho - 1, coluna + 1) + 1):
                if (l, c) in self.__cavado or self.__tabuleiro[l][c] == BOMBA:
                    continue
                self.__cavar(l, c)
        return True

    def __imprimir_tabuleiro(self) -> None:
        print("   ", " ".join([str(i) for i in range(0, self.__tamanho)]))
        print("  +---------------------+")
        for i in range(self.__tamanho):
            print(i, end=" | ")
            for j in range(self.__tamanho):
                if ((i, j) in self.__cavado):
                    print(self.__tabuleiro[i][j], end=" ")
                else:
                    print(" ", end=" ")
            print("|")
        print("  +---------------------+")