from numpy import*
m=array(eval(input("digite os numeros de matricula: ")))
g2=0
for i in range (size(m)):
	if(m[i]%2!=0):
		g2=g2+1
v=zeros(g2, dtype=int)
q=0
for i in range (size(m)):
		if(m[i]%2!=0):
			v[q]=v[q]+m[i]
			q=q+1
print(v)