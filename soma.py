'''
1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?

'''

def calculate_sum() -> int:
    index = 13
    sum_value = 0

    # Loop de 0 até index(13) somando todos os valores
    for control in range(0, index + 1):
        sum_value += control

    return sum_value

# Print do resultado
print(f"Valor da soma: {calculate_sum()}")
