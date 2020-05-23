# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x=int(input("Entre com o numero do dia de hoje: "))
y=int(input("Entre com o numero de dias apos hoje: "))
a=y%7
if((x<0)or(x>6)):
	print("A entrada", x ,"eh invalida")
#(domingo)para valores atribuidos em y abaixo de 7
elif((x==0)and(y==1)):
	print("Hoje eh domingo e o dia futuro eh segunda")
elif((x==0)and(y==2)):
	print("Hoje eh domingo e o dia futuro eh terca")
elif((x==0)and(y==3)):
	print("Hoje eh domingo e o dia futuro eh quarta")	
elif((x==0)and(y==4)):
	print("Hoje eh domingo e o dia futuro eh quinta")	
elif((x==0)and(y==5)):
	print("Hoje eh domingo e o dia futuro eh sexta")
elif((x==0)and(y==6)):
	print("Hoje eh domingo e o dia futuro eh sabado")
elif((x==0)and(y==7)):
	print("Hoje eh domingo e o dia futuro eh domingo")
#(domingo)para valores atribuidos em y acima de 7	
elif((x==0)and(a==1)):
	print("Hoje eh domingo e o dia futuro eh segunda")
elif((x==0)and(a==2)):
	print("Hoje eh domingo e o dia futuro eh terca")
elif((x==0)and(a==3)):
	print("Hoje eh domingo e o dia futuro eh quarta")	
elif((x==0)and(a==4)):
	print("Hoje eh domingo e o dia futuro eh quinta")	
elif((x==0)and(a==5)):
	print("Hoje eh domingo e o dia futuro eh sexta")
elif((x==0)and(a==6)):
	print("Hoje eh domingo e o dia futuro eh sabado")
elif((x==0)and(a==0)):
	print("Hoje eh domingo e o dia futuro eh domingo")
	
#(segunda)para valores atribuidos em y abaixo de 7
elif((x==1)and(y==1)):
	print("Hoje eh segunda e o dia futuro eh terca")
elif((x==1)and(y==2)):
	print("Hoje eh segunda e o dia futuro eh quarta")
elif((x==1)and(y==3)):
	print("Hoje eh segunda e o dia futuro eh quinta")	
elif((x==1)and(y==4)):
	print("Hoje eh segunda e o dia futuro eh sexta")	
elif((x==1)and(y==5)):
	print("Hoje eh segunda e o dia futuro eh sabado")
elif((x==1)and(y==6)):
	print("Hoje eh segunda e o dia futuro eh domingo")
elif((x==1)and(y==7)):
	print("Hoje eh segunda e o dia futuro eh segunda")
#(segunda)para valores atribuidos em y acima de 7	
elif((x==1)and(a==1)):
	print("Hoje eh segunda e o dia futuro eh terca")
elif((x==1)and(a==2)):
	print("Hoje eh segunda e o dia futuro eh quarta")
elif((x==1)and(a==3)):
	print("Hoje eh segunda e o dia futuro eh quinta")	
elif((x==1)and(a==4)):
	print("Hoje eh segunda e o dia futuro eh sexta")	
elif((x==1)and(a==5)):
	print("Hoje eh segunda e o dia futuro eh sabado")
elif((x==1)and(a==6)):
	print("Hoje eh segunda e o dia futuro eh domingo")
elif((x==1)and(a==0)):
	print("Hoje eh segunda e o dia futuro eh segunda")
	
#(terca)para valores atribuidos em y abaixo de 7
elif((x==2)and(y==1)):
	print("Hoje eh terca e o dia futuro eh quarta")
elif((x==2)and(y==2)):
	print("Hoje eh terca e o dia futuro eh quinta")
elif((x==2)and(y==3)):
	print("Hoje eh terca e o dia futuro eh sexta")	
elif((x==2)and(y==4)):
	print("Hoje eh terca e o dia futuro eh sabado")	
elif((x==2)and(y==5)):
	print("Hoje eh terca e o dia futuro eh domingo")
elif((x==2)and(y==6)):
	print("Hoje eh terca e o dia futuro eh segunda")
elif((x==2)and(y==7)):
	print("Hoje eh terca e o dia futuro eh terca")
#(terca)para valores atribuidos em y acima de 7	
elif((x==2)and(a==1)):
	print("Hoje eh terca e o dia futuro eh quarta")
elif((x==2)and(a==2)):
	print("Hoje eh terca e o dia futuro eh quinta")
elif((x==2)and(a==3)):
	print("Hoje eh terca e o dia futuro eh sexta")	
elif((x==2)and(a==4)):
	print("Hoje eh terca e o dia futuro eh sabado")	
elif((x==2)and(a==5)):
	print("Hoje eh terca e o dia futuro eh domingo")
elif((x==2)and(a==6)):
	print("Hoje eh terca e o dia futuro eh segunda")
elif((x==2)and(a==0)):
	print("Hoje eh terca e o dia futuro eh terca")
	
#(quarta)para valores atribuidos em y abaixo de 7
elif((x==3)and(y==1)):
	print("Hoje eh quarta e o dia futuro eh quinta")
elif((x==3)and(y==2)):
	print("Hoje eh quarta e o dia futuro eh sexta")
elif((x==3)and(y==3)):
	print("Hoje eh quarta e o dia futuro eh sabado")	
elif((x==3)and(y==4)):
	print("Hoje eh quarta e o dia futuro eh domingo")	
elif((x==3)and(y==5)):
	print("Hoje eh quarta e o dia futuro eh segunda")
elif((x==3)and(y==6)):
	print("Hoje eh quarta e o dia futuro eh terca")
elif((x==3)and(y==7)):
	print("Hoje eh quarta e o dia futuro eh quarta")
#(quarta)para valores atribuidos em y acima de 7	
elif((x==3)and(a==1)):
	print("Hoje eh quarta e o dia futuro eh quinta")
elif((x==3)and(a==2)):
	print("Hoje eh quarta e o dia futuro eh sexta")
elif((x==3)and(a==3)):
	print("Hoje eh quarta e o dia futuro eh sabado")	
elif((x==3)and(a==4)):
	print("Hoje eh quarta e o dia futuro eh domingo")	
elif((x==3)and(a==5)):
	print("Hoje eh quarta e o dia futuro eh segunda")
elif((x==3)and(a==6)):
	print("Hoje eh quarta e o dia futuro eh terca")
elif((x==3)and(a==0)):
	print("Hoje eh quarta e o dia futuro eh quarta")	

#(quita)para valores atribuidos em y abaixo de 7
elif((x==4)and(y==1)):
	print("Hoje eh quinta e o dia futuro eh sexta")
elif((x==4)and(y==2)):
	print("Hoje eh quinta e o dia futuro eh sabado")
elif((x==4)and(y==3)):
	print("Hoje eh quinta e o dia futuro eh domingo")	
elif((x==4)and(y==4)):
	print("Hoje eh quinta e o dia futuro eh segunda")	
elif((x==4)and(y==5)):
	print("Hoje eh quinta e o dia futuro eh terca")
elif((x==4)and(y==6)):
	print("Hoje eh quinta e o dia futuro eh quarta")
elif((x==4)and(y==7)):
	print("Hoje eh quinta e o dia futuro eh quinta")
#(quinta)para valores atribuidos em y acima de 7	
elif((x==4)and(a==1)):
	print("Hoje eh quinta e o dia futuro eh sexta")
elif((x==4)and(a==2)):
	print("Hoje eh quinta e o dia futuro eh sabado")
elif((x==4)and(a==3)):
	print("Hoje eh quinta e o dia futuro eh domingo")	
elif((x==4)and(a==4)):
	print("Hoje eh quinta e o dia futuro eh segunda")	
elif((x==4)and(a==5)):
	print("Hoje eh quinta e o dia futuro eh terca")
elif((x==4)and(a==6)):
	print("Hoje eh quinta e o dia futuro eh quarta")
elif((x==4)and(a==0)):
	print("Hoje eh quinta e o dia futuro eh quinta")
	
#(sexta)para valores atribuidos em y abaixo de 7
elif((x==5)and(y==1)):
	print("Hoje eh sexta e o dia futuro eh sabado")
elif((x==5)and(y==2)):
	print("Hoje eh sexta e o dia futuro eh domingo")
elif((x==5)and(y==3)):
	print("Hoje eh sexta e o dia futuro eh segunda")	
elif((x==5)and(y==4)):
	print("Hoje eh sexta e o dia futuro eh terca")	
elif((x==5)and(y==5)):
	print("Hoje eh sexta e o dia futuro eh quarta")
elif((x==5)and(y==6)):
	print("Hoje eh sexta e o dia futuro eh quinta")
elif((x==5)and(y==7)):
	print("Hoje eh sexta e o dia futuro eh sexta")
#(sexta)para valores atribuidos em y acima de 7	
elif((x==5)and(a==1)):
	print("Hoje eh sexta e o dia futuro eh sabado")
elif((x==5)and(a==2)):
	print("Hoje eh sexta e o dia futuro eh domingo")
elif((x==5)and(a==3)):
	print("Hoje eh sexta e o dia futuro eh segunda")	
elif((x==5)and(a==4)):
	print("Hoje eh sexta e o dia futuro eh terca")	
elif((x==5)and(a==5)):
	print("Hoje eh sexta e o dia futuro eh quarta")
elif((x==5)and(a==6)):
	print("Hoje eh sexta e o dia futuro eh quinta")
elif((x==5)and(a==0)):
	print("Hoje eh sexta e o dia futuro eh sexta")
	
#(sabado)para valores atribuidos em y abaixo de 7
elif((x==6)and(y==1)):
	print("Hoje eh sabado e o dia futuro eh domingo")
elif((x==6)and(y==2)):
	print("Hoje eh sabado e o dia futuro eh segunda")
elif((x==6)and(y==3)):
	print("Hoje eh sabado e o dia futuro eh terca")	
elif((x==6)and(y==4)):
	print("Hoje eh sabado e o dia futuro eh quarta")	
elif((x==6)and(y==5)):
	print("Hoje eh sabado e o dia futuro eh quinta")
elif((x==6)and(y==6)):
	print("Hoje eh sabado e o dia futuro eh sexta")
elif((x==6)and(y==7)):
	print("Hoje eh sabado e o dia futuro eh sabado")
#(sabado)para valores atribuidos em y acima de 7	
elif((x==6)and(a==1)):
	print("Hoje eh sabado e o dia futuro eh domindo")
elif((x==6)and(a==2)):
	print("Hoje eh sabado e o dia futuro eh segunda")
elif((x==6)and(a==3)):
	print("Hoje eh sabado e o dia futuro eh terca")	
elif((x==6)and(a==4)):
	print("Hoje eh sabado e o dia futuro eh quarta")	
elif((x==6)and(a==5)):
	print("Hoje eh sabado e o dia futuro eh quinta")
elif((x==6)and(a==6)):
	print("Hoje eh sabado e o dia futuro eh sexta")
elif((x==6)and(a==0)):
	print("Hoje eh sabado e o dia futuro eh sabado")	