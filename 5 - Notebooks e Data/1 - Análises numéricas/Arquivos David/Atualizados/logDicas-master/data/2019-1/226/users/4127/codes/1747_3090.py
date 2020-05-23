t=1
s=0

while(t!=0):
	t=int(input("qual a direcaod da lagartixa? "))
	s= s+t
print(s)
if(s<0):
	print("Abaixo")
if(s>0):
	print("Acima")
if(s==0):
	print("Inicial")
	