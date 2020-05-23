t = float(input("digite o tempo de investimento: "))
qf = 1042000
qo = 1500
i = ((qf/qo)**(1/t)) - 1

print(round(i,5))