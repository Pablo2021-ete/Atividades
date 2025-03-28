# Solicita um número inteiro maior que 1
num = int(input("Digite um número inteiro maior que 1: "))

# Verifica se o número é maior que 1
if num <= 1:
    print("Erro: O número deve ser maior que 1.")
else:
    # Verifica se é primo
    primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            primo = False
            break

    # Exibe o resultado
    if primo:
        print(f"{num} é um número primo.")
    else:
        print(f"{num} não é um número primo.")
