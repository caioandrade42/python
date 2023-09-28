import math
import random


class Jogador:
    def __init__(self, letra):
        self.letra = letra

        def get_movimento(self, jogo):
            pass

class JogadorHumano(Jogador):
    def __init__(self, letra):
        super().__init__(letra)

    def get_movimento(self, jogo):
        posicao_valida = False
        valor = None
        while not posicao_valida:
            posicao = input('vez do jogador ' + self.letra + ' jogar. Escolha um movimento (0-8)')

            try:
                valor = int(posicao)
                if valor not in jogo.movimentos_disponiveis():
                    raise ValueError
                posicao_valida = True
            except ValueError:
                print('Posicao invalida, tente novamente')

        return valor


class JogadorAleatorio(Jogador):
    def __init__(self, letra):
        super().__init__(letra)

    def get_movimento(self, jogo):
        quadrado = random.choice(jogo.movimentos_disponiveis())
        return quadrado


class ComputadorInganhavel(Jogador):
    def __init__(self, letra):
        super().__init__(letra)

    def get_movimento(self,jogo):
        if len(jogo.movimentos_disponiveis())==9:
            posicao=random.choice(jogo.movimentos_disponiveis())
        else:
            posicao = self.minimax(jogo,self.letra)['quadrado']
        return posicao

    def minimax(self,estado,jogador):
        max_jogador=self.letra
        min_jogador='O' if jogador =='X' else 'X'

        if estado.ganhador_atual==min_jogador:
            return {'quadrado':None,'placar':1*(estado.num_posicoes_vazias()+1)
            if min_jogador==max_jogador else -1*(estado.num_posicoes_vazias()+1)}
        elif not estado.posicoes_vazias():
            return {'quadrado':None,'placar':0}

        if jogador==max_jogador:
            melhor_movimento = {'quadrado':None,'placar':-math.inf}
        else:
            melhor_movimento={'quadrado':None,'placar':math.inf}
        for possivel_movimento in estado.movimentos_disponiveis():
            estado.fazer_movimento(possivel_movimento,jogador)
            sim_placar = self.minimax(estado,min_jogador)

            estado.tabuleiro[possivel_movimento]=' '
            estado.ganhador_atual=None
            sim_placar['quadrado']=possivel_movimento

            if jogador==max_jogador:
                if sim_placar['quadrado']>melhor_movimento['placar']:
                    melhor_movimento=sim_placar
            else:
                if sim_placar['placar']<melhor_movimento['placar']:
                    melhor_movimento=sim_placar
        return melhor_movimento
