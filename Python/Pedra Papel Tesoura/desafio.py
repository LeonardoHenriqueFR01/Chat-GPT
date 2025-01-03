# Título: Pedra, Papel ou Tesoura - Melhor de 3
# Crie um programa onde o jogador disputa contra o computador em um jogo de Pedra, Papel ou Tesoura no formato melhor de 3.


from random import randint
from time import sleep

def Linhas():
    print('\033[32m-\033[m' * 50)


def Ganho():
    print('\033[32m-\033[m' * 50)
    print(f'\033[4;32m{"VENCEU":^50}\033[m')
    print('\033[32m-\033[m' * 50)


def Perda():
    print('\033[31m-\033[m' * 50)
    print(f'\033[4;31m{"PERDEU":^50}\033[m')
    print('\033[31m-\033[m' * 50)


def Empate():
    print('\033[33m-\033[m' * 50)
    print(f'\033[4;33m{"EMPATE":^50}\033[m')
    print('\033[33m-\033[m' * 50)


vit_user = vit_maquina = 0

jogadas = {1:"PEDRA", 2:"PAPEL", 3:"TESOURA"}


while True:
    print('[ 1 PEDRA ] [ 2 PAPEL ] [ 3 TESOURA ]')
    try:
        user = int(input('[+] Escolha a sua jogada: '))

        if user < 1 or user > 3:
            print('\033[31mEscolha apenas 1, 2 ou 3! Tente novamente.\033[m')
            continue
    
    except ValueError:
        print('\033[31mDigite um número inteiro valido! Tente novamente.\033[m')
        continue

    print('Maquina jogando...')
    sleep(2)

    maquina = randint(1, 3)

    if user == maquina:
        Empate()
        print(f'Você jogou {jogadas[user]} \nA maquina jogou {jogadas[maquina]}')
        Linhas()

    elif (user == 1 and maquina == 3) or (user == 2 and maquina == 1) or (user == 3 and maquina == 2):
        vit_user += 1
        Ganho()
        print(f'Você jogou {jogadas[user]} \nA maquina jogou {jogadas[maquina]}')
        Linhas()

    else:
        vit_maquina += 1
        Perda()
        print(f'Você jogou {jogadas[user]} \nA maquina jogou {jogadas[maquina]}')
        Linhas()
    
    if vit_user >= 2:
        print('Você ganhou a melhor de 3.')
        Linhas()


    elif vit_maquina >= 2:
        print('A maquina ganhou a melhor de 3.')
        Linhas()
        