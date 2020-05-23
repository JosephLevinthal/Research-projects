#Leitura do numero inteiro
n = int(input("Digite um numero inteiro de 0 a 6: "))
f = int(input("Digite um dia no futuro: "))

hj = "domingo"
df = "domingo" 
if(n<0) or (n>6):
	print("A entrada", n, "eh invalida")

elif(n == 0) and (f % 7 == 0):
	print("Hoje eh",hj,"e o dia futuro eh", df)
elif(n == 0) and (f % 7 == 1):
	df = "segunda"
	print("Hoje eh",hj,"e o dia futuro eh", df)	
elif(n == 0) and (f % 7 == 2):
	df = "terca"
	print("Hoje eh",hj,"e o dia futuro eh", df)	
elif(n == 0) and (f % 7 == 3):
	df = "quarta"
	print("Hoje eh",hj,"e o dia futuro eh", df)	
elif(n == 0) and (f % 7 == 4):
	df = "quinta"
	print("Hoje eh",hj,"e o dia futuro eh", df)	
elif(n == 0) and (f % 7 == 5):
	df = "sexta"
	print("Hoje eh",hj,"e o dia futuro eh", df)	
elif(n == 0) and (f % 7 == 6):
	df = "sabado"
	print("Hoje eh",hj,"e o dia futuro eh", df)	
elif(n == 1) and (f % 7 == 0):
	se = "segunda"
	fse = "segunda"
	print("Hoje eh",se,"e o dia futuro eh", fse)
elif(n == 1) and (f % 7 == 1):
	se = "segunda"
	fse = "terca"
	print("Hoje eh",se,"e o dia futuro eh", fse)	
elif(n == 1) and (f % 7 == 2):
	se = "segunda"
	fse = "quarta"
	print("Hoje eh",se,"e o dia futuro eh", fse)	
elif(n == 1) and (f % 7 == 3):
	se = "segunda"
	fse = "quinta"
	print("Hoje eh",se,"e o dia futuro eh", fse)	
elif(n == 1) and (f % 7 == 4):
	se = "segunda"
	fse = "sexta"
	print("Hoje eh",se,"e o dia futuro eh", fse)	
elif(n == 1) and (f % 7 == 5):
	se = "segunda"
	fse = "sabado"
	print("Hoje eh",se,"e o dia futuro eh", fse)	
elif(n == 1) and (f % 7 == 6):
	se = "segunda"
	fse = "domingo"
	print("Hoje eh",se,"e o dia futuro eh", fse)	
elif(n == 2) and (f % 7 == 0):
	te = "terca"
	fte = "terca"
	print("Hoje eh",te,"e o dia futuro eh", fte)		
elif(n == 2) and (f % 7 == 1):
	te = "terca"
	fte = "quarta"
	print("Hoje eh",te,"e o dia futuro eh", fte)		
elif(n == 2) and (f % 7 == 2):
	te = "terca"
	fte = "quinta"
	print("Hoje eh",te,"e o dia futuro eh", fte)		
elif(n == 2) and (f % 7 == 3):
	te = "terca"
	fte = "sexta"
	print("Hoje eh",te,"e o dia futuro eh", fte)		
elif(n == 2) and (f % 7 == 4):
	te = "terca"
	fte = "sabado"
	print("Hoje eh",te,"e o dia futuro eh", fte)		
elif(n == 2) and (f % 7 == 5):
	te = "terca"
	fte = "domingo"
	print("Hoje eh",te,"e o dia futuro eh", fte)		
elif(n == 2) and (f % 7 == 6):
	te = "terca"
	fte = "segunda"
	print("Hoje eh",te,"e o dia futuro eh", fte)		
elif(n == 3) and (f % 7 == 0):
	qa = "quarta"
	fqa = "quarta"
	print("Hoje eh",qa,"e o dia futuro eh", fqa)		
elif(n == 3) and (f % 7 == 1):
	qa = "quarta"
	fqa = "quinta"
	print("Hoje eh",qa,"e o dia futuro eh", fqa)
elif(n == 3) and (f % 7 == 2):
	qa = "quarta"
	fqa = "sexta"
	print("Hoje eh",qa,"e o dia futuro eh", fqa)		
elif(n == 3) and (f % 7 == 3):
	qa = "quarta"
	fqa = "sabado"
	print("Hoje eh",qa,"e o dia futuro eh", fqa)		
elif(n == 3) and (f % 7 == 4):
	qa = "quarta"
	fqa = "domingo"
	print("Hoje eh",qa,"e o dia futuro eh", fqa)		
elif(n == 3) and (f % 7 == 5):
	qa = "quarta"
	fqa = "segunda"
	print("Hoje eh",qa,"e o dia futuro eh", fqa)		
elif(n == 3) and (f % 7 == 6):
	qa = "quarta"
	fqa = "terca"
	print("Hoje eh",qa,"e o dia futuro eh", fqa)
elif(n == 4) and (f % 7 == 0):
	qi = "quinta"
	fqi = "quinta"
	print("Hoje eh",qi,"e o dia futuro eh", fqi)		
elif(n == 4) and (f % 7 == 1):
	qi = "quinta"
	fqi = "sexta"
	print("Hoje eh",qi,"e o dia futuro eh", fqi)		
elif(n == 4) and (f % 7 == 2):
	qi = "quinta"
	fqi = "sabado"
	print("Hoje eh",qi,"e o dia futuro eh", fqi)		
elif(n == 4) and (f % 7 == 3):
	qi = "quinta"
	fqi = "domingo"
	print("Hoje eh",qi,"e o dia futuro eh", fqi)		
elif(n == 4) and (f % 7 == 4):
	qi = "quinta"
	fqi = "segunda"
	print("Hoje eh",qi,"e o dia futuro eh", fqi)		
elif(n == 4) and (f % 7 == 5):
	qi = "quinta"
	fqi = "terca"
	print("Hoje eh",qi,"e o dia futuro eh", fqi)		
elif(n == 4) and (f % 7 == 6):
	qi = "quinta"
	fqi = "quarta"
	print("Hoje eh",qi,"e o dia futuro eh", fqi)		
elif(n == 5) and (f % 7 == 0):
	sx = "sexta"
	fsx = "sexta"
	print("Hoje eh",sx,"e o dia futuro eh", fsx)
elif(n == 5) and (f % 7 == 1):
	sx = "sexta"
	fsx = "sabado"
	print("Hoje eh",sx,"e o dia futuro eh", fsx)	
elif(n == 5) and (f % 7 == 2):
	sx = "sexta"
	fsx = "domingo"
	print("Hoje eh",sx,"e o dia futuro eh", fsx)	
elif(n == 5) and (f % 7 == 3):
	sx = "sexta"
	fsx = "segunda"
	print("Hoje eh",sx,"e o dia futuro eh", fsx)	
elif(n == 5) and (f % 7 == 4):
	sx = "sexta"
	fsx = "terca"
	print("Hoje eh",sx,"e o dia futuro eh", fsx)
elif(n == 5) and (f % 7 == 5):
	sx = "sexta"
	fsx = "quarta"
	print("Hoje eh",sx,"e o dia futuro eh", fsx)
elif(n == 5) and (f % 7 == 6):
	sx = "sexta"
	fsx = "quinta"
	print("Hoje eh",sx,"e o dia futuro eh", fsx)
elif(n == 6) and (f % 7 == 0):
	sa = "sabado"
	fsa = "sabado"
	print("Hoje eh",sa,"e o dia futuro eh", fsa)	
elif(n == 6) and (f % 7 == 1):
	sa = "sabado"
	fsa = "domingo"
	print("Hoje eh",sa,"e o dia futuro eh", fsa)
elif(n == 6) and (f % 7 == 2):
	sa = "sabado"
	fsa = "segunda"
	print("Hoje eh",sa,"e o dia futuro eh", fsa)
elif(n == 6) and (f % 7 == 3):
	sa = "sabado"
	fsa = "terca"
	print("Hoje eh",sa,"e o dia futuro eh", fsa)
elif(n == 6) and (f % 7 == 4):
	sa = "sabado"
	fsa = "quarta"
	print("Hoje eh",sa,"e o dia futuro eh", fsa)
elif(n == 6) and (f % 7 == 5):
	sa = "sabado"
	fsa = "quinta"
	print("Hoje eh",sa,"e o dia futuro eh", fsa)
elif(n == 6) and (f % 7 == 6):
	sa = "sabado"
	fsa = "sexta"
	print("Hoje eh",sa,"e o dia futuro eh", fsa)			