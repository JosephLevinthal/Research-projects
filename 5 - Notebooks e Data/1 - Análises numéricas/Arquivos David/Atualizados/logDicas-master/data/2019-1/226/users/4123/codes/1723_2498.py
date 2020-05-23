na = float(input())
nb = float(input())
ta = float(input())
tb = float(input())

i = 0

while na<nb:
	na+=na*ta/100
	nb+=nb*tb/100
	i+=1
print(i)