# Crie um programa que simule uma conta bancária, onde o usuário pode:
# Depositar um valor
# Sacar um valor
# Consultar o saldo


def Linhas():
    print('\033[32m-\033[m' * 50)


def Sistema_bancario():

    from time import sleep

    saldo = 0.0
    while True:
        print(f'{"Sistema bancario":^40}')
        Linhas()
        print('[ 1 Ver saldo] [ 2 Depositar] [ 3 Sacar] [ 4 Sair]')
        Linhas()

        try:
            escolha = int(input('[+] O que você deseja fazer: '))

            if escolha < 1 or escolha > 4:
                print('\033[31mEscolha apenas 1, 2 ou 3! Tente novamente.\033[m')
                continue

        except ValueError:
            print('\033[31mDigite um número inteiro valido! Tente novamente.\033[m')
            continue
        
        if escolha == 4:
            print('Finalizando...')
            sleep(2)
            break 

        elif escolha == 1:
            print(f'[+] Seu saldo atual e de R${saldo:.2f}')
            Linhas()

        elif escolha == 2:
            while True:
                try:
                    valor = float(input('Digite o valor que deseja depositar: R$'))

                    if valor > 0:
                        saldo += valor
                        print(f'Você depositou um valor de R${valor:.2f}')
                        Linhas()
                        break
                
                except ValueError:
                    print('\033[31mDigite um número inteiro valido! Tente novamente.\033[m')
                    continue
        
        elif escolha == 3:
            while True:
                try:
                    valor = float(input('[+] Digite o valor que deseja sacar: R$'))

                    if valor > saldo:
                        print('\033[31valor para saque indisponivel! Tente consultar primeiro o seu saldo.\033[m')
                        continue

                    saldo -= valor
                
                except ValueError:
                    print('\033[31mDigite um número inteiro valido! Tente novamente.\033[m')
                    continue
                
                print(f'Você sacou um valor de R${valor:.2f}')
                break


Sistema_bancario()
