# Peça ao usuário uma frase e formate todas as palavras como um título, garantindo que a primeira e a última palavra sempre comecem com maiúscula, enquanto palavras intermediárias seguem regras gramaticais.



# Pegando a frase do usuário
frase = str(input('[+] Digite uma frase: ')).title().split()

frase_formatada = " ".join(frase) # Frase formatada

print(frase_formatada) # Mostra a frase formatada
