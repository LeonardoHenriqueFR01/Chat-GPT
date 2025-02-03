# Crie um programa que peça ao usuário três números e retorne o menor número entre eles


while True:
    try:
        n1 = int(input('[+] Digite o 1° valor: '))
        n2 = int(input('[+] Digite o 2° valor: '))
        n3 = int(input('[+] Digite o 3° valor: '))

        if (n1 < n2) and (n1 < n3):
            print(f'[+] O menor valor digitado foi o {n1}')
            break 
        
    except ValueError:
        print('[+] Digite um número inteiro valido! Tente novamente.')
        continue
