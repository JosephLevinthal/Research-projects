from numpy import*
vt = array(eval(input("escreva um vetor: ")))

print(size(vt))
print(vt[0])
print(vt[-1])
print(max(vt))
print(min(vt))
print(sum(vt))

med = sum(vt)/size(vt)
print(round(med,2))