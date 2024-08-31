""" 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média; """

import json

file_path = 'C:\\Users\\LUANF\\Teste-Têcnico\\faturamento_diario.json'

with open(file_path, 'r') as json_file:
    faturamento = json.load(json_file)

def calcula_faturamento(faturamento):
    valores = [valor for valor in faturamento.values() if valor > 0]

    menor_valor = min(valores)
    maior_valor = max(valores)
    
    media_mensal = sum(valores) / len(valores)
    
    dias_acima_media = sum(1 for valor in valores if valor > media_mensal)
    
    return menor_valor, maior_valor, dias_acima_media

menor, maior, dias_acima = calcula_faturamento(faturamento)
print("Resultado:")
print(f"Menor valor de faturamento: {menor}")
print(f"Maior valor de faturamento: {maior}")
print(f"Número de dias com faturamento acima da média: {dias_acima}")

