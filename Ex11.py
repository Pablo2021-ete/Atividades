# Solicita o nome de usuário e a senha
usuario = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")

# Verifica se o usuário e a senha são iguais
while usuario == senha:
    print("Erro: A senha não pode ser igual ao nome de usuário.")
    senha = input("Digite uma nova senha: ")

print("Cadastro realizado com sucesso!")
