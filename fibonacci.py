'''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
'''

def is_fibonacci(number: int) -> int:
    # Inicializa os dois primeiros números de Fibonacci
    a, b = 0, 1

    # Continue adicionando números de Fibonacci até que 'b' seja maior ou igual ao número
    while b < number:
        a, b = b, a + b  # Move to the next Fibonacci number

    # Retorna True se o número for encontrado na sequência ou se o número for 0
    return b == number or number == 0

while True:
    try: 
        # Input: numero
        num = int(input("Digite um number: "))
        break
    except(ValueError): 
        print("Insira um número!")

# Verifique se o número pertence à sequência de Fibonacci
if is_fibonacci(num):
    print(f"{num} está na sequência de Fibonacci.")
else:
    print(f"{num} não está na sequência de Fibonacci.")
