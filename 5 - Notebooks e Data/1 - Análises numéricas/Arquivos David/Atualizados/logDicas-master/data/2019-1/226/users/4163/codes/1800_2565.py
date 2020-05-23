from numpy import*

mf = array(eval(input("media final: ")))
fre = array(eval(input("frequencia: ")))
ch = int(input("carga horaria: "))

re =  zeros(3, dtype=int)
a = 0.75 * ch

for i in range(size(mf)):
	if(mf[i] >= 5 and fre[i] >= a) and (mf[i]<=10 and fre[i]<= ch):
		re[0]= re[0] + 1
	elif (mf[i]<5 and fre[i]>= a and(mf[i]>=0) and fre[i]>=0):
		re[1] = re[1] + 1
	elif(fre[i]>=0 and fre[i]<a):
		re[2] = re[2] + 1
print(re)
		
	
