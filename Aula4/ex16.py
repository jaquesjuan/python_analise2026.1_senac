valor1 = float(input("Digite um valor: " ))
valor2 = float(input("Digite mais um valor: " ))
valor3 = float(input("Digite outro valor: " ))
if valor1 > valor2 and valor1 > valor3:
    print(f"O maior valor entre os três é o primeiro: {valor1}")
elif valor2 > valor1 and valor2 > valor3:
    print(f"O maior valor entre os três é o segundo: {valor2}")
else:
    print(f"O maior valor é o terceiro: {valor3}")