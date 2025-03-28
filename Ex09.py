# Solicita três números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Determina o maior e o menor número
maior = max(num1, num2, num3)
menor = min(num1, num2, num3)

# Exibe os resultados
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
