# Solicita as três notas do usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média aritmética simples
media_aritmetica = (nota1 + nota2 + nota3) / 3

# Calcula a média ponderada com pesos 2, 2 e 3
media_ponderada1 = (nota1 * 2 + nota2 * 2 + nota3 * 3) / (2 + 2 + 3)

# Calcula a média ponderada com pesos 1, 2 e 2
media_ponderada2 = (nota1 * 1 + nota2 * 2 + nota3 * 2) / (1 + 2 + 2)

# Exibe os resultados
print(f"Média Aritmética Simples: {media_aritmetica:.2f}")
print(f"Média Ponderada (pesos 2,2,3): {media_ponderada1:.2f}")
print(f"Média Ponderada (pesos 1,2,2): {media_ponderada2:.2f}")
