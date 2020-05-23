from math import*
p = int(input()) #pontos de vida iniciais
D1 = int(input())
D2 = int(input())
d = p - int((sqrt(5 * D1) + pi**(D2//3))) 
print(int(d))