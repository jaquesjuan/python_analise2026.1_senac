ano_nascimento = int(input("Em que ano você nasceu? "))
ano_atual = int(input("Em que ano estamos? "))
idade = ano_atual - ano_nascimento
if idade < 0:
        print(f"Você errou algo! Faça novamente!")
        if idade >= 18 > 0:
            print(f"Você tem {idade} anos. É maior de idade!")
else:
    print(f"Você tem {idade} anos. É menor de idade!")