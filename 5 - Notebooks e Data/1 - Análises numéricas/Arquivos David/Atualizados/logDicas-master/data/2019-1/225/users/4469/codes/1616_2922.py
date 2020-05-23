t  = float(input("Tempo de investimento: "))

i = ((1042000.0/1500.0) ** (1/t)) - 1

print(round(i, 5))