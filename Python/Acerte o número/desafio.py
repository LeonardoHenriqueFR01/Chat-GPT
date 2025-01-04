# Desenvolva um jogo onde o computador escolhe um número aleatório entre 1 e 100, e o usuário tenta adivinhar. 
# Informe se o palpite é maior ou menor até acertar.


from random import randint
from time import sleep


def Acerte_num():
    maquina = randint(1, 101)
    while True:
        try:
            num_user = int(input('Digite um número de 1 a 100: '))
        
        except ValueError:
            print('\033[31mDigite um número inteiro valido! Tente novamente.\033[m')
            continue
        
        print('Gerando número da maquina...')
        sleep(2)

        if num_user == maquina:
            print(f'O número sorteado foi {maquina} você acertou.')
        
        elif num_user < maquina:
            print(f'E maior do que {num_user}! Tente novamente.')

        elif num_user > maquina:
            print(f'E menor do que {num_user}! Tente novamente.')

Acerte_num()
