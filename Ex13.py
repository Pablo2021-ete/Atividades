# Solicita o salário inicial e o número de anos
salario = float(input("Digite o salário inicial (R$): "))
aumento_percentual = float(input("Digite o aumento percentual inicial (%): ")) / 100
anos = int(input("Digite a quantidade de anos: "))

# Calcula o salário ano a ano
for ano in range(1, anos + 1):
    salario *= (1 + aumento_percentual)
    aumento_percentual *= 2  # O aumento dobra a cada ano

# Exibe o salário final
print(f"O salário após {anos} anos será de R${salario:.2f}")
