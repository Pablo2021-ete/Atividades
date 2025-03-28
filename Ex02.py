# Solicita o valor em segundos
segundos = int(input("Digite o tempo em segundos: "))

# Calcula dias, horas, minutos e segundos restantes
dias = segundos // 86400  # 1 dia tem 86400 segundos
resto = segundos % 86400

horas = resto // 3600  # 1 hora tem 3600 segundos
resto = resto % 3600

minutos = resto // 60  # 1 minuto tem 60 segundos
segundos_restantes = resto % 60

# Exibe os resultados
print(f"{segundos} segundos equivalem a: {dias} dias, {horas} horas, {minutos} minutos e {segundos_restantes} segundos.")
