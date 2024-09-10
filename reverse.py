'''
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
'''

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
