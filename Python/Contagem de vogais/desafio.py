# Crie um programa onde o usuário digita uma frase, e o programa conta quantas vogais (a, e, i, o, u) existem nela, ignorando maiúsculas e minúsculas.


def Verifica_vogais(texto):
    vogais = 'aeiouAEIOU'
    
    for letra in texto:
    
        if letra in vogais:
            return True
    
    return False


texto = str(input('Digite uma frase: '))
if Verifica_vogais(texto):
    print('O texto contem Vogal.')

else:
    print('O texto não contem Vogal.')

