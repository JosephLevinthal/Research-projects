qidf=int(input("q inicial d deus forseti:"))
qidl=int(input("q inicial d deus loki:"))
pacf=float(input("percentual de crescimento forseti:"))
pacl=float(input("percentual de crescimento loki:"))
pacf=pacf/100
pacl=pacl/100

cont=0

while(qidl!=qidf and qidl<qidf):
	qidf=((qidf*pacf-qidf))
	qidl=((qidl*pacl-qidf))
	cont=cont+1*12
print(cont)