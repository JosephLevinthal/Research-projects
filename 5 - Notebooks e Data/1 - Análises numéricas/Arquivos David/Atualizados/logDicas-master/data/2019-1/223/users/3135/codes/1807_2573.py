from numpy import*
vp= array(eval(input("Insira o peso dos alunos:")))
vh= array(eval(input("Insira a altura dos alunos:")))
a=0
imc=zeros(size(vh), dtype=float)

for i in range(size(vp)) and range(size(vh)):	
	imc[i]=vp[i]/(vh[i]*vh[i])
	imc[i]=round(imc[i],2)
print(imc)
print("O MAIOR IMC DA TURMA EH:", max(imc))

if(max(imc) < 17):
	print("muito abaixo do peso".upper())
elif(max(imc)>=17 and max(imc)<=18.49):
	print("abaixo do peso".upper())
elif(max(imc)>=18.5 and max(imc)<=24.99):
	print("peso normal".upper())
elif(max(imc)>=25 and max(imc)<= 29.99):
	print("acima do peso".upper())
elif(max(imc)>=30 and max(imc)<=3 4.99):
	print("obesidade".upper())
elif(max(imc)>= 35 and max(imc) <= 39,99):
	print("obesidade severa".upper())
elif(max(imc) > 40):
	print("obesidade morbida".upper())