n=int(input(""))
s=0
i = 1
il=0
p=0
w=0
r=0
while (p<n):
	t=(2*il+ 1)
	r=4/t
	w=(-1)**(i+1)*r
	s=s+w
	i = i + 1
	p=p+1
	il=il+1
# Impressao de resultados
print(round(s,8))
