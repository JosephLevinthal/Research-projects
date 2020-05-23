t = float(input("tempo de investimento: "))
i = round((1.042/1.5**(1/t))-1,5)
print(float(round(i,5)))