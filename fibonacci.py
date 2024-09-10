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
