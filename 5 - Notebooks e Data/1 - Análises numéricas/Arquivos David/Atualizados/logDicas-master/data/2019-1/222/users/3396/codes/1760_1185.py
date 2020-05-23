from  numpy import *

n = array(eval(input("Digite as glicoses:")))
i = 0
cont = 0

while size(n) > i:
    if n[i] > 99:
        print(i)
        i = i +1
        cont =cont + 1
    else: 
        i = i + 1
print(cont)
