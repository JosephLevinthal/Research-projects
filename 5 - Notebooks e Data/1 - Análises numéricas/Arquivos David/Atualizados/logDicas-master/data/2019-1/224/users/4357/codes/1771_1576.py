from numpy import*
vetor0 = array(eval(input("Vetor0: ")))
vetor1 = array(eval(input("Vetor1: ")))
i=0
e=0
a=0
while(i < size(vetor0) and vetor0!= vetor1):
	i = i + 1
if(size(vetor0) < size(vetor1)):
	mensagem="EUSAPIA"
print(mensagem)
elif(size(vetor0) > size(vetor1)):
	mensagem="BERSANULFO"
print(mensagem)
else:
	mensagem="EMPATE"
print(mensagem)
print(size(vetor1+vetor0))
	