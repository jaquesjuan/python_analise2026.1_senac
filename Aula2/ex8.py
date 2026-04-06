valor1 = float(input("Insira o valor do produto: "))
valor2 = float(input("Insira a porcentagem de desconto desejada: "))
desconto = (valor1 * valor2) / 100
valor_final = valor1 - desconto
print(f"{valor2}% de {valor1} é: {desconto} ")
print(f"Preço c/ desconto: {valor_final}")