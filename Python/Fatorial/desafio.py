# Escreva um programa que receba um número inteiro e calcule seu fatorial.

def Fato():
    global n
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
            if n < 0:
                print('\033[31mDigite um número que não seja negativo! Tente novamente.\033[m')
                continue
                
            fato = 1
            for i in range(1, n + 1):
                fato *= i 

            return fato

        except ValueError:
            print('\033[31mDigite um número inteiro valido! Tente novamente.\033[m')
            continue
    

resul = Fato()
print(f'O fatorial de {n} é {resul}')
