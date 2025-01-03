# Peça ao usuário para digitar uma palavra e verifique se ela é um palíndromo (lê-se igual de trás para frente).

def obter_frase():
    while True:
        global frase
        try:
            frase = str(input('Digite uma frase e veja se ela e um Palíndromo: ')).capitalize().replace(" ", "")

            if any(char.isdigit()  for char in frase):
                raise ValueError('\033[31mNúmeros não são permitidos na String! Tente novamente.\033[m')
            return frase 

        except ValueError as e:
            print(e)


obter_frase()
frase_invertida = frase[::-1].capitalize().replace(" ", "")

if frase_invertida == frase:
    print(f'{frase} é um Palíndromo.')

else:
    print(f'{frase} não é um Palíndromo.')