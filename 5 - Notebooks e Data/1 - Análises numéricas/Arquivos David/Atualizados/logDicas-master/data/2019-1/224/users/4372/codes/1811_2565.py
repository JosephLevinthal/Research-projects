from numpy import*
mf=array(eval(input("digite as medias finais: ")))
p=array(eval(input("digite as medias finais: ")))
ch=int(input("digite a carga horaria: "))
er=zeros(3, dtype=int)
for i in range(size(mf)):
	if(mf[i]>=5) and (p[i]>=(ch*(75/100))):
		er[0]=er[0]+1
	if(mf[i]<5):
		er[1]=er[1]+1
	if(p[i]<(ch*(75/100))):
		er[2]=er[2]+1
print(er)