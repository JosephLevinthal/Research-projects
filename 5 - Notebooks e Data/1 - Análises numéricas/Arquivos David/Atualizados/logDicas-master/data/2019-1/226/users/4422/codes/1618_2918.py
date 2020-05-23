valorint = float(input("Valor do ingreco: "))
quantidade = int(input("Quantos ingrecos: "))
desconto = 20
precopromocional = valorint - (valorint*(desconto/100))
valortot = precopromocional * quantidade
print(round(valortot, 2))