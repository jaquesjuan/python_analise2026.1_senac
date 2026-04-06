#identação
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
if media >= 6:
    print(f"A sua média foi {media}. Parabéns! Aprovado!")
else:
    print(f"A sua média foi {media}. Não foi dessa vez... Tentaremos novamente na recuperação!")