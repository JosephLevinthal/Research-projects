from numpy import *
pre = array(eval(input("")))
fal = array(eval(input("")))
pre = pre - fal
maior = 0
for i in range(1,len(pre)):
	if pre[maior]<pre[i]:
		maior = i
print(maior+1)