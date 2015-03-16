from random import shuffle

lista_armas = ['PEDRA','PAPEL','TESOURA','LAGARTO','SPOCK']
lista_armas = lista_armas*2
nj = 0
nc = 0

def jogador_win():
    global nj
    global nc
    print('\nO jogador venceu a partida.')
    nj += 1
    nc = 0

def computador_win():
    print('\nO computador venceu a partida.')
    global nj
    global nc
    nc += 1
    nj = 0

while nc < 3 and nj < 3:
    for x in range(4):
        shuffle(lista_armas)
    pc = lista_armas[6]
    print('\nComputador pronto.')
    jogador = input('Escolha entre PEDRA, PAPEL, TESOURA, LAGARTO e SPOCK (em letras maiúsculas): ')
    print('Escolha do Computador: %s'%pc)
    if pc == jogador:
        print('\nEMPATE')
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
    elif jogador == 'stop':
        break
    else:
        print('\nOpção Inválida.')
if nj == 3:
    print('\nO jogador ganhou o jogo!')
elif nc == 3:
    print('\nO computador ganhou o jogo!')
else:
    print('\nJogador desistiu. Volte sempre.')
