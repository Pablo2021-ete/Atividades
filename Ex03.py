# Solicita o valor total das mercadorias compradas
valor_total = float(input("Digite o valor total das mercadorias compradas (R$): "))

# Define o limite e a taxa de imposto
limite = 500
taxa_imposto = 0.5  # 50%

# Calcula o imposto apenas sobre o valor que ultrapassar R$500
if valor_total > limite:
    valor_excedente = valor_total - limite
    imposto = valor_excedente * taxa_imposto
else:
    imposto = 0

# Exibe os resultados
print(f"Valor total da compra: R${valor_total:.2f}")
print(f"Imposto a ser pago: R${imposto:.2f}")
