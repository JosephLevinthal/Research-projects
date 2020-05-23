# Ao testar sua solução, não se limite ao caso de exemplo.
X=float(input("coordenada x:"))
Y=float(input("coordenada y:"))
Q1=X>0 and Y>0
Q2=Y>0 and X<0
Q3=X<0 and Y<0
Q4=Y<0 and X>0

if(X>0 and Y>0):
	r="Q1"
elif(Y>0 and X<0):
	r="Q2"
elif(X<0 and Y<0):
	r="Q3"
elif(Y<0 and X>0):
	r="Q4"
elif(X>0 and Y==0 or X<0 and Y==0):
	r="Eixo X"
elif(X==0 and Y>0 or X==0 and Y<0):
	r="Eixo Y"
else:
	r="Origem"
print(r)