genero = input("Qual o seu gênero? 'M' ou 'F' > ")
idade = int(input("Digite sua idade: "))
if genero == "M" and idade >= 18:
    print("Você está apto a se alistar!")
else:
    print("Você não está apto a se alistar!")