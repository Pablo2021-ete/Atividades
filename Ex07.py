# Solicita um número ímpar ao usuário
num = int(input("Digite um número ímpar: "))

# Verifica se o número é realmente ímpar
if num % 2 == 0:
    print("Erro: O número digitado não é ímpar.")
else:
    num_anterior = num - 2  # Número ímpar anterior
    num_proximo = num + 2  # Próximo número ímpar

    # Calcula os quadrados
    quadrado_anterior = num_anterior ** 2
    quadrado_proximo = num_proximo ** 2

    # Calcula a diferença
    diferenca = quadrado_proximo - quadrado_anterior

    # Exibe os resultados
    print(f"Número ímpar anterior: {num_anterior}")
    print(f"Número ímpar seguinte: {num_proximo}")
    print(f"Quadrado de {num_anterior}: {quadrado_anterior}")
    print(f"Quadrado de {num_proximo}: {quadrado_proximo}")
    print(f"Diferença entre os quadrados: {diferenca}")
