from numpy import*

time1=array(eval(input("n gols time 1:")))
time2=array(eval(input("n gols time 2:")))

x = zeros(3, dtype=int)

for i in range(size(time1)):
	if (time1[i] > time2[i]):
			x[0]=x[0]+1
	if (time1[i] == time2[i]):
			x[1]=x[1]+1
	if (time1[i] < time2[i]):
			x[2]= x[2]+1
print(x)		
		
		