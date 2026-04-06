temp = float(input("Digite a temperatura no momento: "))
if temp > 24:
    print("Esta temperatura é considerada calor!")
elif temp >= 1 and temp <= 18 or temp <=0:
    print("Esta temperatura é considerada frio!")
else:
    print("Esta temperatura é considerada agradável!")