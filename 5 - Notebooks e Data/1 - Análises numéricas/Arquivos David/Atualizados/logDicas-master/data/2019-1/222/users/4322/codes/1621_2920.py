prato = float(input("quantas gramas seu prato tem? "))
bebidas = int(input("quantas bebidas? "))
doce = int(input("quantos doces? "))
valorfinal = 26.90 * (prato / 1000) + 3.50 * bebidas + 3.0 * doce
print(round(valorfinal, 2))