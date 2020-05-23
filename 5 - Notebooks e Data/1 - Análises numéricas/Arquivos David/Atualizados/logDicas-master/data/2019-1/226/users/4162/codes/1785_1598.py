from numpy import*
p=array(eval(input("insira os custos dos itens: ")))
s=0
q=0
i=0
while i!=size(p):
	if p[i]>80:
		q=(p[i]-5)
	else:
		q=p[i]
	s=s+q
	i=i+1
print(round(s,2))