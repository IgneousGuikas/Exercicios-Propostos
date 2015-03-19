from random import shuffle
from colorama import Fore

lista_armas = ['PEDRA','PAPEL','TESOURA','LAGARTO','SPOCK']
lista_armas = lista_armas*2
nj = 0
nc = 0
game_in = 'sim'

def jogador_win():
    global nj
    global nc
    print('\nO ' + Fore.RED + 'jogador ' + Fore.BLACK + 'venceu a partida.')
    nj += 1
    nc = 0

def computador_win():
    global nj
    global nc
    print('\nO ' + Fore.BLUE + 'computador ' + Fore.BLACK + 'venceu a partida.')
    nc += 1
    nj = 0

print(Fore.RED + """
            JOGO PEDRA, PAPEL, TESOURA, LAGARTO E SPOCK""" + Fore.BLACK)
while game_in == 'sim':
    while nc < 3 and nj < 3:
        for x in range(4):
            shuffle(lista_armas)
        pc = lista_armas[6]
        print(Fore.BLUE + '\n\nComputador ' + Fore.BLACK + 'pronto.')
        jogador = input('Escolha entre PEDRA, PAPEL, TESOURA, LAGARTO e SPOCK: ').upper()
        print('Escolha do ' + Fore.BLUE + 'Computador' + Fore.BLACK + ': %s'%pc)
        if jogador == 'STOP':
            break
        elif pc == jogador:
            print(Fore.GREEN + '\nEMPATE' + Fore.BLACK)
        elif jogador == 'PEDRA':
            if (pc == 'PAPEL') or (pc == 'SPOCK'):
                computador_win()
            elif (pc == 'TESOURA') or (pc == 'LAGARTO'):
                jogador_win()
        elif jogador == 'PAPEL':
            if (pc == 'TESOURA') or (pc == 'LAGARTO'):
                computador_win()
            elif (pc == 'PEDRA') or (pc == 'SPOCK'):
                jogador_win()
        elif jogador == 'TESOURA':
            if (pc == 'PEDRA') or (pc == 'SPOCK'):
                computador_win()
            elif (pc == 'PAPEL') or (pc == 'LAGARTO'):
                jogador_win()
        elif jogador == 'LAGARTO':
            if (pc == 'TESOURA') or (pc == 'PEDRA'):
                computador_win()
            elif (pc == 'PAPEL') or (pc == 'SPOCK'):
                jogador_win()
        elif jogador == 'SPOCK':
            if (pc == 'PAPEL') or (pc == 'LAGARTO'):
                computador_win()
            elif (pc == 'PEDRA') or (pc == 'TESOURA'):
                jogador_win()
        else:
            print('\nOpção Inválida.')
    if nj == 3:
        print('\nO ' + Fore.RED + 'jogador ' + Fore.BLACK + 'ganhou o jogo!')
    elif nc == 3:
        print('\nO ' + Fore.BLUE + 'computador ' + Fore.BLACK + 'ganhou o jogo!')
    else:
        print(Fore.RED + '\nJogador ' + Fore.BLACK + 'desistiu. Volte sempre.')
        break
    game_in = input(Fore.RED + 'Deseja jogar de novo (sim ou não): ' + Fore.BLACK).lower()
