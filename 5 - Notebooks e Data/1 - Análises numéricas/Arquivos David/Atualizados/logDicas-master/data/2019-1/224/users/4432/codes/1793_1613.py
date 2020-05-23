from numpy import*
va=input("atividades").upper()
v=(eval(input("vetor  ")))
x=0
i=0
s=0
cont=0
while(i<size(v)):
	i=i+1
	if va[s]=='ALONGAMENTO':
		cont=cont+v[x]*3
	elif va[s]=='CORRIDA' :
		cont=cont+v[x]*10.3
	elif va[s]=='DANCA' :
		cont=cont+(v[x]*6.7)
	elif va[s]=='ESCALADA' :
		cont=cont+v[x]*9.7
	s=s+1
	x=x+1
print(cont)