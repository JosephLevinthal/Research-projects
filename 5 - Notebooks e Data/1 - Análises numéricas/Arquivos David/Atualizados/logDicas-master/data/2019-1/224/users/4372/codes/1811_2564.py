from numpy import*
a=array(eval(input("digite os gols por partida: ")))
b=array(eval(input("digite os gols por partida: ")))
er=zeros(3, dtype=int)
for i in range(size(a)):
	if(a[i]>b[i]):
		er[0]=er[0]+1
	if(a[i]==b[i]):
		er[1]=er[1]+1
	if(a[i]<b[i]):
		er[2]=er[2]+1
print(er)