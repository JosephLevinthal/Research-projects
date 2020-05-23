from numpy import*
x=array(eval(input("Digite o primeiro jogador: ")))
y=array(eval(input("Digite o segundo jogador: ")))
t=0
h=0
while(size(x)>h):
	if(x[h]==1):
		t=t+40
		h=h+1
	elif(x[h]==2):
		t=t+20
		h=h+1
	elif(x[h]==3):
		t=t+10
		h=h+1
	elif(x[h]>=4):
		t=t+0
		h=h+1
r=0
h=0
while(size(x)>h):
	if(y[h]==1):
		r=r+40
		h=h+1
	elif(y[h]==2):
		r=r+20
		h=h+1
	elif(y[h]==3):
		r=r+10
		h=h+1
	elif(y[h]>=4):
		r=r+0
		h=h+1


if(t>r):
	print("JOGADOR UM")
elif(r>t):
	print("JOGADOR DOIS")
else:
	print("EMPATE")
	
"leel"
	

	
	
		
	
	
		
		
		