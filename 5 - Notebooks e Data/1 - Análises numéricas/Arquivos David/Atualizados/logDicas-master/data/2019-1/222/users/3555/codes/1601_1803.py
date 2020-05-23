i=int(input())
# n4 n3 n2 n1 

n4 = i//1000
n3 = (i % 1000) // 100
n2 = (i%100)//10 
n1 = (i%10) // 1

soma = (n1*2) + (n2*3) + (n3*4) + (n4*5)
verificador = soma % 11
print(verificador)


