# Solicita a quantidade de turmas
turmas = int(input("Digite a quantidade de turmas: "))

# Lista para armazenar a quantidade de alunos por turma
alunos_por_turma = []

# Solicita a quantidade de alunos para cada turma
for i in range(1, turmas + 1):
    alunos = int(input(f"Digite a quantidade de alunos na turma {i}: "))
    alunos_por_turma.append(alunos)
    
    # Verifica se a turma tem mais de 40 alunos
    if alunos > 40:
        print(f"Atenção: A turma {i} tem mais de 40 alunos!")

# Calcula a média de alunos por turma
media_alunos = sum(alunos_por_turma) / turmas

# Exibe o resultado
print(f"Média de alunos por turma: {media_alunos:.2f}")
