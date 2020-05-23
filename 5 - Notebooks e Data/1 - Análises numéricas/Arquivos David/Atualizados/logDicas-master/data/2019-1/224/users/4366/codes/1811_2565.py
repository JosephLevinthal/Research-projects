from numpy import *
media_final=array(eval(input("digite as medias finais:")))
frequencia=array(eval(input("digite a frequencia:")))
carga_horaria=float(input("digite a carga horaria:"))
v=zeros(3, dtype=int)
r=carga_horaria*75/100
for i in range(size(media_final)):
	if(media_final[i]>=5) and (frequencia[i]>=r):
		v[0]=v[0]+1
	if(media_final[i]<5):
		v[1]=v[1]+1
	if(frequencia[i]<r):
		v[2]=v[2]+1
print(v)
			 
			 
			 
			 