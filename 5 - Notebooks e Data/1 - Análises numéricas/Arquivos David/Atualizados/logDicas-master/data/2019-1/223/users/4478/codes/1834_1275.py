from numpy import*
from numpy.linalg import*

func = array(eval(input("horas trabalhadas em cada dia da semana:")))
vetor = zeros(func.shape[0], dtype=int)

for i in range (func.shape[0]):
	vetor[i] = sum(func[i,:])
print(vetor)
