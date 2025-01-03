# Peça um número ao usuário e informe se ele é primo ou não.

def eh_primo(n):
    if n <= 1:
        return False  
    for i in range(2, int(n ** 0.5) + 1):  
        if n % i == 0:  
            return False
    return True  

while True:
    try:
        numero = int(input("Digite um número: "))
    
    except ValueError:
        print('\033[31mDigite um número inteiro valido! Tente novamente.\033[m')
        continue

    if eh_primo(numero):
        print(f"{numero} é primo!")

    else:
        print(f"{numero} não é primo.")
