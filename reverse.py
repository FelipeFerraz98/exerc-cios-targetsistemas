def reverse_string(text : str) -> str:
    reversed_text = '' # Inicializa uma string vazia

    # Loop pela string original do fim ao começo
    for index in range(len(text) - 1, -1, -1):
        reversed_text += text[index]  # Adiciona caractere da string de maneira reversa

    return reversed_text

# Input: insira a string
input_string = input("Insira a string: ")

# Print a string reversed
print(f"Reversed string: {reverse_string(input_string)}")
