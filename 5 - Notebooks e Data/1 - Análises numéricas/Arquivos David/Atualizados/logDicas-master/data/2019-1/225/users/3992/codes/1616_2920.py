var1 = float(input("peso do prato:"))
var2 = float(input("quantidade de bebidas:"))
var3 = float(input("quantidade de sobremesas:"))

pp = (var1/1000)*26.90
ps = var2*3.50
pb = var3*3
pf = pp+ps+pb
print(round(pf, 2))