from numpy import *
ve = array(eval(input("jogadas de Eusapia: ")))
vb = array(eval(input("jogadas de Barsanulfo: ")))
i = 0
soma_e = 0
soma_b = 0
valor_e = 0
valor_b = 0
while(i < size(ve)):
	if(ve[i] == 33 and vb[i] == 22):
		valor_e = 1
		valor_b = 0
	elif(ve[i] == 22 and vb[i] == 11):
		valor_e = 1
		,
		valor_b = 0
	elif(ve[i] == 11 and vb[i] == 33):
		valor_e = 1
		valor_b = 0
	elif(ve[i] == 11 and vb[i] == 11):
		valor_e = 0
		valor_b = 0
	elif(ve[i] == 22 and vb[i] == 22):
		valor_e = 0
		valor_b = 0
	elif(ve[i] == 33 and vb[i] == 33):
		valor_e = 0
		valor_b = 0
	elif(ve[i] == 22 and vb[i] == 33):
		valor_b = 1
		valor_e = 0
	elif(ve[i] == 33 and vb[i] == 11):
		valor_b = 1
		valor_e = 0
	elif(ve[i] == 11 and vb[i] == 22):
		valor_b = 1
		valor_e = 0
	soma_b = soma_b + valor_b
	soma_e = soma_e + valor_e
	i = i + 1
print(size(ve))
if(soma_b == soma_e):
	print("EMPATE")
if(soma_b>soma_e):
	print("BARSANULFO")
if(soma_e>soma_b):
	print("EUSAPIA")