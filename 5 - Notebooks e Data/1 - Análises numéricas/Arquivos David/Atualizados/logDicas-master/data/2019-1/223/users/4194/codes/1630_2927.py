bebida=float(input("Qual o valor da bebida?"))
esfirras=int(input("Quantas esfirras comprou?"))

preco=float(1.5)
total=round(esfirras*preco+bebida, 2)
print(total)