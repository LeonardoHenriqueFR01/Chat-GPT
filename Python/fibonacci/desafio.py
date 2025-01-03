# Crie um programa que exiba os n primeiros números da sequência de Fibonacci.

def fibonacci(n):
    a, b = 0, 1
    
    for _ in range(n):
        a, b = b, a + b
    
    return a

for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")
