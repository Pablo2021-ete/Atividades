def eh_primo(n):
    """Função para verificar se um número é primo."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Lista para armazenar os primeiros 100 números primos
primos = []
num = 2  # Primeiro número a ser verificado

while len(primos) < 100:
    if eh_primo(num):
        primos.append(num)
    num += 1

# Exibe os 100 primeiros números primos
print(*primos)
