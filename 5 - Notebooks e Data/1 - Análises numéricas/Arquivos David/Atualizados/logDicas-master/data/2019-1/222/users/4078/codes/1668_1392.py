cliente = float(input("consumo de agua: "))
taxa = 30
if(cliente >= 10**3):
   print(round(3 *(cliente) + taxa),2)
else:
   print(round(3.5*(cliente) + 30),2)