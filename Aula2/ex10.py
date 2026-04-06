nome_cliente = input("Nome do cliente: ")
ano_nascimento = int(input("Ano de nascimento: "))
ano_atual = int(input("Em que ano estamos? "))
idade_atual = ano_atual - ano_nascimento
print(f"Olá, {nome_cliente}! Você tem {idade_atual} anos!")