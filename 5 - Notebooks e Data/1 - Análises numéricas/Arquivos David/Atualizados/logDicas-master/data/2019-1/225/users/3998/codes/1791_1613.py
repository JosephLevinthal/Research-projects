from numpy import*
t = array(eval(input())).upper
m= int(input())  #duração da atividade

i = 0
l = 0

while(m > i):
	if(t[i] == "ALONGAMENTO"):
		l = m[i] * 3
		i = i +1
	elif(t[i]== "CORRIDA"):
		l= m[i] * 10.3
		i= i+1
	elif(t[i]=="DANCA"):
		l= m [i] * 6.7
		i=i+1
	elif(t[i]=="ESCADA"):
		l= m [i] * 9.7
		i=i+1
	elif(t[i]=="HIDROGINASTICA"):
		l= m [i] * 5
		i=i+1

		print(round(i,2)