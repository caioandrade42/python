import time
import math

from jogador import JogadorHumano, JogadorAleatorio, ComputadorInganhavel


class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = self.fazer_tabuleiro()
        self.ganhador_atual = None

    @staticmethod
    def fazer_tabuleiro():
        return [' ' for _ in range(9)]

    def imprimir_tabuleiro(self):
        for linha in [self.tabuleiro[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(linha) + ' |')

    @staticmethod
    def imprime_numeros_tabuleiro():
        numeros_tabuleiro = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for linha in numeros_tabuleiro:
            print('| ' + ' | '.join(linha) + ' |')

    def faz_movimento(self, posicao, letra):
        if self.tabuleiro[posicao] == ' ':
            self.tabuleiro[posicao] == letra
            if self.vencedor(posicao,letra):
                self.ganhador_atual=letra
            return True
        return False

    def movimentos_disponiveis(self):
        movimentos = []
        for (i, posicao) in enumerate(self.tabuleiro):
            if posicao == ' ':
                movimentos.append(i)
        return movimentos

    def posicoes_vazias(self):
        return ' ' in self.tabuleiro

    def num_posicoes_vazias(self):
        return self.tabuleiro.count(' ')

    def fazer_movimento(self, posicao, letra):
        if self.tabuleiro[posicao] == ' ':
            self.tabuleiro[posicao] = letra
            if self.ganhador(posicao, letra):
                self.ganhador_atual = letra
            return True
        else:
            return False


    def ganhador(self, posicao, letra):
        linha_index = math.floor(posicao/3)
        linha = self.tabuleiro[linha_index * 3:(linha_index + 1) * 3]
        if all([quadrado == letra for quadrado in linha]):
            return True

        index_coluna = posicao % 3
        coluna = [self.tabuleiro[index_coluna + i * 3] for i in range(3)]
        if all([quadrado == letra for quadrado in coluna]):
            return True

        if posicao % 2 == 0:
            diagonal1 = [self.tabuleiro[i] for i in [0, 4, 8]]
            if all(quadrado == letra for quadrado in diagonal1):
                return True
            diagonal2 = [self.tabuleiro[i] for i in [2, 4, 6]]
            if all(quadrado == letra for quadrado in diagonal2):
                return True

        return False

def jogar(jogo, jogador_x, jogador_o, imprimir_tabuleiro=True):
    if imprimir_tabuleiro:
        jogo.imprime_numeros_tabuleiro()
    letra = 'X'

    while jogo.posicoes_vazias():
        if letra == 'O':
            posicao = jogador_o.get_movimento(jogo)
        else:
            posicao = jogador_x.get_movimento(jogo)

        if jogo.fazer_movimento(posicao, letra):
            if imprimir_tabuleiro:
                print(letra + f' Realiza um movimento na posicao {posicao}')
                jogo.imprimir_tabuleiro()
                print('')

            if jogo.ganhador_atual:
                if imprimir_tabuleiro:
                    print('JOGADOR ' + letra + ' VENCEU!')
                return letra

            if letra == 'X':
                letra = 'O'
            else:
                letra = 'X'

            time.sleep(0.5)

    if imprimir_tabuleiro:
        print('DEU VELHA')


if __name__ == '__main__':
    jogador_x = JogadorHumano('X')
    jogador_o = ComputadorInganhavel('O')
    jogo_da_velha = JogoDaVelha()
    jogar(jogo_da_velha, jogador_x, jogador_o, imprimir_tabuleiro=True)
