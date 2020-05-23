from numpy import*
a=array(eval(input("digite o vetor: ")))
b=array(eval(input("digite o vetor: ")))
i=0
sa=0
sb=0
while(i<size(a)):
	if(a[i]==1):
		sa=sa+40
	if(a[i]==2):
		sa=sa+20
	if(a[i]==3):
		sa=sa+10
	if(a[i]==4):
		sa=sa+0
	if(b[i]==1):
		sb=sb+40
	if(b[i]==2):
		sb=sb+20
	if(b[i]==3):
		sb=sb+10
	if(b[i]==4):
		sb=sb+0
	i=i+1
if(sa==sb):
	print("EMPATE")
if(sa>sb):
	print("JOGADOR UM")
if(sa<sb):
	print("JOGADOR DOIS")