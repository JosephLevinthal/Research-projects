from numpy import*

Time1 = array(eval(input()))
Time2 = array(eval(input()))
i = 0
placar = zeros((3,), dtype=int)

while(i < size(Time1)):
	if(Time1[i] > Time2[i] ): placar[0]+=1
	elif(Time1[i] == Time2[i]): placar[1]+=1
	else: placar[2]+=1
	i+=1
	
print(placar)