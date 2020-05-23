from numpy import*
mf=array(eval(input("vetor de medias finais: ")))
f=array(eval(input("vetor de frequencia: ")))
c=int(input("carga horaria: "))
a=0
rn=0
rf=0
i = 0
pfm=(c*75)/100
for v in mf:
	if (mf[i]>=5 and f[i]>=pfm):
		a= a + 1
		i= i + 1
	elif (mf[i]<5):
		rn= rn + 1
		i = i + 1
	elif (f[i]<pfm):
		rf= rf + 1
		i= i + 1
total=zeros(3, dtype=int)
total[0]=a
total[1]=rn
total[2]=rf
print(total)