valor = float(input("Qual o valor da mercadoria? R$"))
if valor >= 500:
    print(f"O valor pós desconto é: {valor * 0.80}")
elif valor >= 100 and valor <= 499:
    print(f"O valor pós desconto é: {valor * 0.75}")
else:
    print(f"O valor pós desconto é: {valor * 0.95}")

    # Sugestão: delimitar variáveis como desconto e porcentagens para possíveis análises e manipulações futuras. Gera mais dados, porém mais manipulável.