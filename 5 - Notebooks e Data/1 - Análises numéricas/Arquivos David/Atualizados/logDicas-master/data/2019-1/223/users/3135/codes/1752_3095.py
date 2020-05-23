r= input("Insira o resultado do campeonato:").upper()
v=0
d=0
e=0

while(r!="X"):
	if(r=="V"):
		v=v+3
	elif(r=="E"):
		e=e+2
	elif(r=="D"):
		d=d+1
	r=input("Insira seu resultado:").upper()

print(v)
print(e)
print(d)