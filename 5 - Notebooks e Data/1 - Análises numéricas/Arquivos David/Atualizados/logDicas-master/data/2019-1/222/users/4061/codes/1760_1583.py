from numpy import *

N = input("digite caracteres: ")
N1 = len(N)
S1 = N[0:3]
I = 3

while(I < N1):
	S1 = S1 + "."+ N[I:I + 3]
	I=I+3
print(S1)