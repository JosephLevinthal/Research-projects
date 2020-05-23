time = float(input("Tempo:"))
h1 = (time*100) #PRA SEPARAR OS MINUTOS EM h2
h2 = (h1%100) #SEPARA OS MINUTOS
h3 = (h2/60) #PARTE REAL DOS MINUTOS
h4 = int((time)) #SEPARA AS HORAS
h5 = (h4+h3) #SOMA AS HORAS COM AS PARTES REAIS DOS MINUTOS (horas em número real)
spd = float(input("Velocidade:"))
dist = (spd*time)
qtdl = (dist/12)
print(round(dist, 3))
print(round(qtdl, 3))