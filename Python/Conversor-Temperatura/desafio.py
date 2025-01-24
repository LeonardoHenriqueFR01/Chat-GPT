# Conversor de temperatura

from time import sleep


# Função para mostrar opções de conversão
def Mostrar_opcoes_conversao(opcoes):
    print(f'[+] {opcoes}')



# Função para converter Celsius para Fahrenheit
def Cel_Fah():
    while True:
        try:
            celcius = float(input('[+] Digite °C: '))
            convertido = celcius * 9 / 5 + 32

            print('[+] Fazendo operação...')
            sleep(2)

            print(f'[+] {celcius}° convertidos para Fahrenheit ficará: {convertido:.2f}')
            break

        
        except ValueError:
            print('[+] \033[31mDigite um número inteiro valido! Tente novamente.\033[m')
            continue


# Função para converter Celsius para Kelvin
def Cel_Kel():
    while True:
        try:
            celcius = float(input('[+] Digite °C: '))
            convertido = celcius + 273.15

            print('[+] Fazendo operação...')
            sleep(2)

            print(f'[+] {celcius}° convertidos para Kelvin ficará: {convertido:.2f}')
            break
        
        except ValueError:
            print('[+] \033[31mDigite um número inteiro valido! Tente novamente.\033[m')
            continue


# Função para converter Fahrenheit para Celcius
def Fah_Cel():
    while True:
        try:
            fahrenheit = float(input('[+] Digite °C: '))
            convertido = (fahrenheit - 32) * 5 / 9

            print('[+] Fazendo operação...')
            sleep(2)

            print(f'[+] {fahrenheit}° convertidos para Celsius ficará: {convertido:.2f}')
            break
        
        except ValueError:
            print('[+] \033[31mDigite um número inteiro valido! Tente novamente.\033[m')
            continue


# Função para converter Fahrenheit para Kelvin
def Fah_Kel():
    while True:
        try:
            fahrenheit = float(input('[+] Digite °C: '))
            convertido = (fahrenheit - 32) * 5 / 9 + 273.15

            print('[+] Fazendo operação...')
            sleep(2)

            print(f'[+] {fahrenheit}° convertidos para Kelvin ficará: {convertido:.2f}')
            break
        
        except ValueError:
            print('[+] \033[31mDigite um número inteiro valido! Tente novamente.\033[m')
            continue


# Função para converter Kelvin para Celcius
def Kel_Cel():
     while True:
        try:
            kelvin = float(input('[+] Digite °C: '))
            convertido = kelvin - 273.15

            print('[+] Fazendo operação...')
            sleep(2)

            print(f'[+] {kelvin}° convertidos para Celcius ficará: {convertido:.2f}')
            break
        
        except ValueError:
            print('[+] \033[31mDigite um número inteiro valido! Tente novamente.\033[m')
            continue    


# Função para converter Kelvin para Fahrenheit
def Kel_Fah():
    while True:
        try:
            kelvin = float(input('[+] Digite °C: '))
            convertido = (kelvin - 273.15) * 9 / 5 + 32

            print('[+] Fazendo operação...')
            sleep(2)

            print(f'[+] {kelvin}° convertidos para Fahrenheit ficará: {convertido:.2f}')
            break
        
        except ValueError:
            print('[+] \033[31mDigite um número inteiro valido! Tente novamente.\033[m')
            continue    


while True:
    try:
        print('[+] \033[31m[ 0 SAIR ]\033[m [ 1 Celsius ] [ 2 Fahrenheit ] [ 3 Kelvin ]') 
        temperatura = int(input('[+] Escolha a temperatura: '))

        if temperatura == 0:
            print('[+] Finalizando...')
            sleep(2)
            break

        elif temperatura not in [1, 2, 3]:
            print('[+] \033[31mEscolha apenas 0, 1, 2 ou 3! Tente novamente.\033[m')
            continue

        elif temperatura == 1:
            Mostrar_opcoes_conversao('[+] [ 1 Fahrenheit ] [ 2 Kelvin ]')
        elif temperatura == 2:
            Mostrar_opcoes_conversao('[+] [ 1 Celcius ] [ 2 Kelvin ]')
        elif temperatura == 3:
            Mostrar_opcoes_conversao('[+] [ 1 Celcius ] [ 2 Fahrenheit ]')

        while True:
            try:
                escolha = int(input('[+] Para qual você deseja fazer a conversão: '))

                if escolha not in[1, 2]:
                    print('[+] \033[31mEscolha apenas 1 ou 2! Tente novamente.\033[m')
                    continue

                elif temperatura == 1 and temperatura == 1:
                    Cel_Fah()
                    break
                elif temperatura == 1 and temperatura == 2:
                    Cel_Kel()
                    break
                elif temperatura == 2 and temperatura == 1:
                    Fah_Cel()
                    break
                elif temperatura == 2 and temperatura == 2:
                    Fah_Kel()
                    break
                elif temperatura == 3 and temperatura == 1:
                    Kel_Cel()
                    break
                elif temperatura == 3 and temperatura == 2:
                    Kel_Fah()
                    break

            except ValueError:
                print('[+] \033[31mDigite um número inteiro valido! Tente novamente.\033[m')
                continue


    except ValueError:
        print('[+] \033[31mDigite um número inteiro valido! Tente novamente.\033[m')
        continue
