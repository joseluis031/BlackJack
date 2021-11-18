cartas = {chr(0x1f0a1): 11,
    chr(0x1f0a2): 2,
    chr(0x1f0a3): 3,
    chr(0x1f0a4): 4,   #A cada key(azul) le corresponde un valor(el numero) y 1f0a..es la representacion grafica de la carta
    chr(0x1f0a5): 5,
    chr(0x1f0a6): 6,
    chr(0x1f0a7): 7,
    chr(0x1f0a8): 8,
    chr(0x1f0a9): 9,
    chr(0x1f0aa): 10,
    chr(0x1f0ab): 10,
    chr(0x1f0ad): 10,
    chr(0x1f0ae): 10,}

print("Cartas: {}".format(" ".join(cartas.keys())))
print("Puntos: {}".format(list(cartas.values()))) #Con esto consigo que el programa me de las diferentes cartas y los puntos posibles que he definido en la lista

print("1\ Iteración estándar sobre un diccionario")
for carta, valor in cartas.items():               #Aqui se define carta como el valor de cada item de la lista cartas
    print("la carta {} vale {}".format(carta, valor)) #Con esto consigo darle a cada carta el valor correspondiente

print("2\ Iteración ordenada sobre un diccionario")
for carta in sorted(cartas.keys()):
    print("la carta {} vale {}".format(carta, cartas[carta]))