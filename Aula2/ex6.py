# input permite que o usuário insira dados
altura_cliente = float(input("Digite sua altura: "))
peso_cliente = float(input("Digite seu peso: "))
imc = peso_cliente / (altura_cliente * altura_cliente)
print(f"O índice IMC do aluno é {imc}")