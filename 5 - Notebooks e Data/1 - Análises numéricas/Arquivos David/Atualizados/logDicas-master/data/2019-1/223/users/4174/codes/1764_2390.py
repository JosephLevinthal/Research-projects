from numpy import*

f = array(eval(input("frequencia:")))
mf = max(f)

i = 0
mes = 0
while(i < size(f)):
	if(f[i] == mf):
		mes = i + 1
	i = i + 1
print(mes)