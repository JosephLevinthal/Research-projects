fish = int(input())
perc = int(input())
mes = 0
c2 = perc/100

while 0 < fish < 8000:
	ret = int(input())
	acr = fish * c2
	fish = fish + acr
	fish = fish - ret
	mes += 1
if (fish <= 0):
	print("ZERO")
else:
	print("MAXIMO")
print(mes)