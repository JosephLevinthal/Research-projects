senha=int(input("insira sua senha:"))
du=senha%10
du1=senha//10
du2=du1%10
du3=senha//100
du4=du3%10
du5=senha//1000
du6=du5%10
du7=senha//10000
du8=du7%10
du9=senha//100000
du10=du9%10
s=du8+du4+du
s1=du2+du6+du10
if(s%s1 == 0):
	msg="acesso liberado"
else:
	msg="senha invalida"