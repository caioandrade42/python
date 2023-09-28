import random


def jogo():
    usuario = input("Digite '1' para pedra, '2' para papel, '3' para tesoura: ")
    computador = random.choice(['1', '2', '3'])
    print(vitoria_jogador(usuario, computador))
    jogar_novamente = input("Deseja jogar novamente? 's'/'n': ")
    if jogar_novamente == 's':
        return jogo()
    else:
        return None


def vitoria_jogador(jogador1, jogador2):
    if jogador1 == '1' and jogador2 == '2':
        return 'Papel cobre pedra, Computador venceu'
    elif jogador1 == '1' and jogador2 == '3':
        return 'Pedra esmaga tesoura, Jogador venceu'
    elif jogador1 == '2' and jogador2 == '1':
        return 'Papel cobre pedra, Jogador venceu'
    elif jogador1 == '2' and jogador2 == '3':
        return 'Tesoura corta papel, Computador venceu'
    elif jogador1 == '3' and jogador2 == '1':
        return 'Pedra esmaga tesoura, Computador venceu'
    elif jogador1 == '3' and jogador2 == '2':
        return 'Papel cobre pedra, Computador venceu'
    elif jogador1 == jogador2:
        return 'Empate!'


jogo()