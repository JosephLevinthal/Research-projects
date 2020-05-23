# Ao testar sua solução, não se limite ao caso de exemplo.
m=int(input("mes do ano:"))
if(1<=m<=12):
	if(m==1):
		s="janeiro"
	elif(m==2):
		s="fevereiro"
	elif(m==3):
		s="marco"
	elif(m==4):
		s="abril"
	elif(m==5):
		s="maio"
	elif(m==6):
		s="junho"
	elif(m==7):
		s="julho"
	elif(m==8):
		s="agosto"
	elif(m==9):
		s="setembro"
	elif(m==10):
		s="outubro"
	elif(m==11):
		s="novembro"
	else:
		s="dezembro"
else:
	s="numero de mes invalido"
print(s)