qnt = int(input())
perc = int(input())
ret = int(input())
ano = 0
f = perc/100
while 0 < qnt < 12000:
	acre = qnt * f
	qnt = acre + qnt
	qnt = qnt - ret
	ano += 1
if(qnt <= 0):
	print("EXTINCAO")
else:
	print("LIMITE")
print(ano)
	