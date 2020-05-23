from numpy import*
v = array(eval(input("vetor: ")))
c = v**7
m = (sum(c)/size(v))**(1/7)
print(round(m, 2))