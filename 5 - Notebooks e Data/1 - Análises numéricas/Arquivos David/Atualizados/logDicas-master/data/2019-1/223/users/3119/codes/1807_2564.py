from numpy import*

time = array(eval(input("Digite os gols do time da casa: ")))
time1 = array(eval(input("Digite os gols do time adversario: ")))

cont = zeros(3, dtype = int)

for i in range(size(time1)):
	if(time[i] > time1[i]):
		cont[0] = cont[0] + 1
	elif(time[i] == time1[i]):
		cont[1] = cont[1] + 1
	elif(time[i] < time1[i]):
		cont[2] = cont[2] + 1
		
print(cont)		