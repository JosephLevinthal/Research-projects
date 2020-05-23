from numpy import*

e = array(eval(input("Qtd entraram: ")))
s = array(eval(input("Qtd sairam: ")))

l = e[0] - s[0] + e[1] - s[1] + e[2] - s[2] + e[3] - s[3]

print(sum(l))