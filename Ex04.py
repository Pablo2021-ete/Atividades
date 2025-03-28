# Solicita os dados do cliente
dias = int(input("Quantos dias o carro foi alugado? "))
km_rodados = float(input("Quantos quilômetros foram percorridos? "))

# Definição dos custos
custo_diario = 90  # Custo por dia de aluguel
limite_km = 100  # Limite de km sem taxa extra
taxa_extra = 12  # Taxa por km adicional

# Calcula o custo base
custo_base = dias * custo_diario

# Verifica se há taxa extra
if km_rodados > limite_km:
    km_excedente = km_rodados - limite_km
    custo_extra = km_excedente * taxa_extra
else:
    custo_extra = 0

# Calcula o valor total
valor_total = custo_base + custo_extra

# Exibe os resultados
print(f"Valor do aluguel: R${custo_base:.2f}")
print(f"Taxa por km extra: R${custo_extra:.2f}")
print(f"Valor total a pagar: R${valor_total:.2f}")
