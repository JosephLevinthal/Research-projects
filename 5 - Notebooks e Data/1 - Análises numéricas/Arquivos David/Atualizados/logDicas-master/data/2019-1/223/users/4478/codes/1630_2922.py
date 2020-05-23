m = float(input("tempo de investimento:"))
acum = 1042000
inic = 1500
x = acum/inic
taxa = x**(1/m)
i = taxa-1

print(round(i, 5))