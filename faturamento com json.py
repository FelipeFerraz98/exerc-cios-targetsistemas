'''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
'''

import json

def analyze_revenue(file_path: str) -> int:
    # Abra e leia o arquivo JSON
    with open(file_path, 'r') as file:
        data = json.load(file)["revenue"]

    # Filtrar dias sem faturamento
    revenue_days = [rev for rev in data if rev > 0]

    # Calcular o faturamento mínima, máxima e média
    min_revenue = min(revenue_days)
    max_revenue = max(revenue_days)
    average_revenue = sum(revenue_days) / len(revenue_days)

    # Conte o número de dias em que a faturamento ficou acima da média
    days_above_average = len([rev for rev in revenue_days if rev > average_revenue])

    return min_revenue, max_revenue, days_above_average

# Chame a função e exiba os resultados
file_path = 'daily_revenue.json'  # Caminho para o arquivo JSON
min_revenue, max_revenue, days_above_average = analyze_revenue(file_path)

print(f"Menor Faturamento: {min_revenue}")
print(f"Maior Faturamento: {max_revenue}")
print(f"Dias acima da média: {days_above_average}")
