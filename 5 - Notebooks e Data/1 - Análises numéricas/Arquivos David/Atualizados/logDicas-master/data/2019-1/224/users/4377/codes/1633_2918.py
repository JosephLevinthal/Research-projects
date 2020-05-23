preco=float(input("integral"))
quant=int(input("quantidade"))
desconto=20/100
precopromocional=preco-(preco*(desconto))
total=precopromocional*quant
print(round(total,2))