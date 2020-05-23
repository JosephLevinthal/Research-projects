from numpy import*

no = array(eval(input("notas:")))
fr = array(eval(input("frequencia:")))
ch = int(input("carga horaria:"))

x = zeros(3, dtype = int)
#apr = ch * (75/100)
for i in range(size(no)):
	if no[i] >= 5 and fr[i] >= ch * (75/100):
		x[0] = x[0] + 1
	elif no[i] < 5 and fr[i] >= ch * (75/100):
		x[1] = x[1] + 1
	elif no[i] >= 5 and fr[i] < ch * (75/100):
		x[2] =x[2] +1
print(x)