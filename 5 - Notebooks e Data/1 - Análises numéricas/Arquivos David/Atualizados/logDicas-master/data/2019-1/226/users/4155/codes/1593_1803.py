num = int(input("valor: "))
mil = num // 1000
restm = num % 1000
cem = restm // 100
restc = restm % 100
dez = restc // 10
um = restc % 10
a1 = um * 2 + dez * 3 + cem * 4 + mil * 5
a2 = a1 % 11
print(a2)


