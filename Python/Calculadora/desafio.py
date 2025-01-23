# Crie uma calculadora que permite ao usuário escolher entre quatro operações matemáticas (adição, subtração, multiplicação e divisão). 

from time import sleep


# Função para operador de +
def Adicao():
    while True:
        try:
            num_1 = int(input('[+] Digite o 1° valor: '))
            num_2 = int(input('[+] Dgiite o 2° valor: '))
            soma = num_1 + num_2
            print('[+] Somando valores...')
            sleep(2)
            print(f'[+] A soma de {num_1} + {num_2} = {soma:.2f}')

            opcao = int(input('[+] [ 0 SAIR ] [ 1 CONTINUAR ]: '))

            if opcao < 0 or opcao > 1:
                print('[+] \033[31mDigite apenas 0 ou 1! Tente novamente.\033[m')
                continue

            elif opcao == 0:
                break

            elif opcao == 1:
                continue

        except ValueError:
            print('[+] \033[31mDigite um número inteiro valido! Tente novamente.\033[m')
            continue            


# Função para operador de -
def Subtrair():
    while True:
        try:
            num_1 = int(input('[+] Digite o 1° valor: '))
            num_2 = int(input('[+] Dgiite o 2° valor: '))
            soma = num_1 - num_2
            print('[+] Somando valores...')
            sleep(2)
            print(f'[+] A soma de {num_1} - {num_2} = {soma:.2f}')

            opcao = int(input('[+] [ 0 SAIR ] [ 1 CONTINUAR ]: '))

            if opcao < 0 or opcao > 1:
                print('[+] \033[31mDigite apenas 0 ou 1! Tente novamente.\033[m')
                continue

            elif opcao == 0:
                break

            elif opcao == 1:
                continue

        except ValueError:
            print('[+] \033[31mDigite um número inteiro valido! Tente novamente.\033[m')
            continue    


# Função para operador de *
def Multiplica():
    while True:
        try:
            num_1 = int(input('[+] Digite o 1° valor: '))
            num_2 = int(input('[+] Dgiite o 2° valor: '))
            soma = num_1 * num_2
            print('[+] Somando valores...')
            sleep(2)
            print(f'[+] A soma de {num_1} * {num_2} = {soma:.2f}')

            opcao = int(input('[+] [ 0 SAIR ] [ 1 CONTINUAR ]: '))

            if opcao < 0 or opcao > 1:
                print('[+] \033[31mDigite apenas 0 ou 1! Tente novamente.\033[m')
                continue

            elif opcao == 0:
                break

            elif opcao == 1:
                continue

        except ValueError:
            print('[+] \033[31mDigite um número inteiro valido! Tente novamente.\033[m')
            continue    


# Função para operador de /
def Dividir():
    while True:
        try:
            num_1 = int(input('[+] Digite o 1° valor: '))
            num_2 = int(input('[+] Dgiite o 2° valor: '))
            soma = num_1 / num_2
            print('[+] Somando valores...')
            sleep(2)
            print(f'[+] A soma de {num_1} / {num_2} = {soma:.2f}')

            opcao = int(input('[+] [ 0 SAIR ] [ 1 CONTINUAR ]: '))

            if opcao < 0 or opcao > 1:
                print('[+] \033[31mDigite apenas 0 ou 1! Tente novamente.\033[m')
                continue

            elif opcao == 0:
                break

            elif opcao == 1:
                continue

        except ValueError:
            print('[+] \033[31mDigite um número inteiro valido! Tente novamente.\033[m')
            continue    


# Função para fazer operações
def Opera():
    while True:
        try:
            print('\033[31m[ 0 SAIR ]\033[m [ 1 + ] [ 2 - ] [ 3 * ] [ 4 / ]')
            escolha = int(input('[+] Escolha uma das opções: '))

            if escolha == 0:
                print('[+] Finalizando programa...')
                sleep(3)
                break
            
            elif escolha < 0 or escolha > 4:
                print('[+] \033[31mEscolha apenas 1, 2, 3, 4, 5 ou zero para sair! Tente novamente.\033[m')
                continue

            elif escolha == 1:
                Adicao()

            elif escolha == 2:
                Subtrair()

            elif escolha == 3:
                Multiplica()

            elif escolha == 4:
                Dividir()

        except ValueError:
            print('[+] \033[31mDigite um número inteiro valido! Tente novamente.\033[m')
            continue


Opera()
