sp = si = ci = cp = 0
while 1:
	n = int(input())
	if n==0:
		break
	elif n%2==0:
		sp += n
		cp += 1
	else:
		si +=n
		ci +=1
if cp!=0:
	print(round(sp/cp,2))
else:
	print(0.0)
if ci!=0:
	print(round(si/ci,2))
else:
	print(0.0)