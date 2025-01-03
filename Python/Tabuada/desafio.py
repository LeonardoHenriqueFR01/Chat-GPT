# Solicite um número inteiro ao usuário e exiba a tabuada desse número de 1 a 10.

while True:
    try:
        num = int(input('Digite um número e veja a tabuada de 10 dele: '))

    except ValueError:
        print('\033[31mDigite um número inteiro valido! Tente novamente.\033[m')
        continue

    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')
       