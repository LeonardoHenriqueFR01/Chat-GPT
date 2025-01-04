


def Count_pares():
    while True:
        try:
            num = int(input('Digite um número: '))
        
        except ValueError:
            print('\033~[31mDigite um número inteiro valido! Tente novamente.\033[m')
            continue

        if num % 2 == 0:
            print(f'{num} é um número PAR.')
        
        elif num % 2 == 1:
            print(f'{num} é um número IMPAR.')

Count_pares()
