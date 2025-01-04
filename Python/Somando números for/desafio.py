# Crie um programa que receba um número inteiro positivo do usuário e calcule a soma de todos os números de 1 até o número informado.
# Por exemplo:
# Se o usuário digitar 5, o programa deve somar 1 + 2 + 3 + 4 + 5 e exibir o resultado final.



def Soma_num():
    while True:
        try:
            num = int(input('Digite um número inteiro: '))
        
        except ValueError:
            print('\033[31mDigite um número inteiro valido! Tente novamente.\033[m')
            continue

        for i in range(1, num + 1):
            print(f'{i}')