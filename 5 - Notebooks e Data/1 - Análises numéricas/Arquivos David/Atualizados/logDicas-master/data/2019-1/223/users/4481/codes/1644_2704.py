media= float(input("nota do aluno"))
med = input("recebera bonificacao ? (S/N) ")
if( med.upper() == "S"):  
	total = media + media*10/100
else:
	total = media
print(round(total,2))
