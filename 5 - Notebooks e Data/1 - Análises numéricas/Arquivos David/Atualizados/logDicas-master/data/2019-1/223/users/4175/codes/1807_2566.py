from numpy import *

x = array(eval(input()))

y = zeros(6)

for i in range(size(x)):
	if x[i] == 2:
		y[0] += 1
	if x[i] == 3:
		y[1] += 1
	if x[i] == 4:
		y[2] += 1
	if x[i] == 5:
		y[3] += 1
	if x[i] == 6:
		y[4] += 1
	if x[i] == 7:
		y[5] += 1


for i in range(size(y)):
	y[i]=round(y[i]/size(x)*100,1)
print(y)
