from numpy import*
v = array(eval(input("Digite o vet: ")))
v = v[0:-1] > 0
n = size(v)
me = ((v[0:-1]** 7) / n) ** 1/7
print(me)