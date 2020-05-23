from numpy import*
x = array(eval(input("custo de itens: ")))

i = 0


while (i<size(x)):
	i = i + 1
b = 0 #entrada
a = 0 #saida
lis = zeros(i , dtype=float)

while(a<size(lis)):
	if x[a] < 80:
		d = x[a]-5
		d = lis[b]
		a = a + 1
		b = b + 1
	else:
		lis[b] = x[a]
		a = a +1
		b = b +1
comp = sum(lis)
print(comp)		
print(lis)
	