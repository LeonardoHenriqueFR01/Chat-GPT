# Crie um programa que peça dois números ao usuário e exiba a soma deles.

while True:
        for i in range(1):
                try:
                    n1 = int(input(f'Digite o 1° número: '))

                except ValueError:
                       print('\033[31m Digite um número inteiro valido! Tente novamente.\033[m')
                       continue
                
                try:    
                    n2 = int(input(f'Digite o 2°número: '))
                
                except ValueError:
                    print('\033[31m Digite um número inteiro valido! Tente novamente.\033[m')
                    continue

                print(f'A soma de {n1} + {n2} = {n1 + n2}')
