# Tipos de triângulos


def ladostriangulo():
    while True:
        try:
            n1 = int(input('[+] Digite o 1° lado: '))
            n2 = int(input('[+] Digite o 2° lado: '))
            n3 = int(input('[+] Digite o 3° lado: '))

            # Verificando se os lados formam um triângulo
            if (n1 + n2 > n3) and (n1 + n3 > n2) and (n2 + n3 > n1):
                # Classificação do triângulo
                if n1 == n2 == n3:
                    print('É um Equilátero.')
                elif n1 == n2 or n1 == n3 or n2 == n3:
                    print('É um Isósceles.')
                else:
                    print('É um Escaleno.')
                break
            else:
                print('[!] Esses valores não formam um triângulo. Tente novamente.')

        except ValueError:
            print('[+] Digite um número inteiro válido! Tente novamente.')

ladostriangulo()
