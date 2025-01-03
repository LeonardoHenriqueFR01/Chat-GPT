# Faça um programa que exiba uma contagem regressiva de 10 até 0, com intervalos de 1 segundo.

from time import sleep

while True:
    try:
        num = int(input('Digite um número e veja a conmtagem regressiva dele: '))
    
    except ValueError:
        print('\033[31mDigite um número inteiro valido! Tente novamente.\033[m')
        continue
    
    for i in range(num, -1, -1):
        print(i)
        sleep(1)
