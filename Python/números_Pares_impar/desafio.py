# Escreva um programa que receba um número inteiro do usuário e informe se ele é par ou ímpar.

while True:
    try:
        num = int(input('Digite um número inteiro é veja se ele e Impar ou Par: '))
    
        if num % 2 == 0:
            print(f'O número que você digitou foi {num} ele e PAR.')

        else:
            print(f'O número que você digitou é IMPAR.')

    except ValueError:
        print('\033[31mDigite um número inteiro valido! Tente novamente.\033[m')
        continue
    