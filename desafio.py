

def ladostriangulo():
    while True:
        try:
            n1 = int(input('[+] Digite o 1° lado: '))
            n2 = int(input('[+] Digite o 2° lado: '))
            n3 = int(input('[+] Digite o 3° lado: '))

            if (n1 == n2) and (n1 == n3) and (n2 == n3):
                print('É um Equilátero.')
                break

            elif (n1 == n2) and (n1 != n3):
                print('É um Esósceles.')
                break
            
            elif (n1 != n2) and (n1 != n3) and (n2 != n3):
                print('É um Escaleno') 
                break
        
        except ValueError:
            print('[+] Digite um número inteiro valido! Tente novamente.')
            continue

ladostriangulo()
