# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x=float(input("Consumo de energia:"))
y=input("tipo de instalacao: (R/I/C)? ")
print("Entradas:",x, "kWh e tipo", y)
if (x<0) or (y != "R") and (y != "I") and (y != "C"):
 print ("Dados invalidos")
elif(y == "R") and (x<=500):
 z= x * 0.44
 print ("Valor total: R$", round (z,2))
elif(y=="R") and (x>500):
 z = x * 0.65
 print("Valor total: R$", round(z,2))
elif(y=="C") and (x<=1000):
 z = x * 0.55
 print("Valor total: R$", round(z,2))
elif(y=="C") and (x>1000):
 z = x * 0.60
 print("Valor total: R$", round(z,2))
elif(y=="I") and (x<=5000): 
 z = x * 0.55
 print("Valor total: R$", round(z,2))
elif(y=="I") and (x>5000):
 z = x * 0.60 
 print("Valor total: R$", round(z,2))
