venda=int(input("Vendas/Dia: "))
lucro=float(venda*12)
lucrototal=(lucro-83/100)*100

despesas=float(100+(lucro-20/100))

valor=round(lucrototal-despesas,2)

print(valor)




