from random import choice, sample #choice(elegir) and sample(para barajar) son lo que voy a utilizar de la libreria random
cartas = {chr(0x1f0a1): 11, #Este es el diccionario
    chr(0x1f0a2): 2,
    chr(0x1f0a3): 3,
    chr(0x1f0a4): 4,   #A cada key(chr) le corresponde un valor(el numero) y 0x1f0a..es la representacion grafica de la carta
    chr(0x1f0a5): 5,
    chr(0x1f0a6): 6,
    chr(0x1f0a7): 7,   #Si cambio {} por ] puedo darle mas de 1 valor a cada key
    chr(0x1f0a8): 8,
    chr(0x1f0a9): 9,
    chr(0x1f0aa): 10,
    chr(0x1f0ab): 10,
    chr(0x1f0ad): 10,
    chr(0x1f0ae): 10,}

print("Cartas: {}".format(" ".join(cartas.keys()))) # .format me da q todo lo q haya dentro del () me lo da entre las {} anterior. .keys para que me de las key de las cartas. join para unir el blanco con el resto
print("Puntos: {}".format(list(cartas.values()))) #Con esto consigo que el programa me de las diferentes cartas y los puntos posibles que he definido en la lista. list para que me lo de en una lista lo q tenia en un diccionario

print("1\ Iteración estándar sobre un diccionario")
for carta, valor in cartas.items():               #Aqui se define carta como el valor de cada item de la lista cartas. Quiero recorrer mi diccionario cartas y que me de un valor(para eso se utiliza item)
    print("la carta {} vale {}".format(carta, valor)) #Con esto consigo darle a cada carta el valor correspondiente
#Para que nos salga valor por valor, 1 por 1.  .items coge una carta(empieza por 0 a no ser que dentro del parentesis le pongas un numero). El for lo que hace es recorrer todo tu diccionario
print("2\ Iteración ordenada sobre un diccionario")
for carta in sorted(cartas.keys()): #para que me salgan los valores segun el orden que yo defina, carta[cartas] es de mi diccionario que se llama cartas, la carta que asocie el valor que le estoy dando, me las ordenara de menor a mayor(por defecto) o de mayor a menor. shorted es para ordenar las cartas
    print("la carta {} vale {}".format(carta, cartas[carta]))

print("Comienza Black Jack:")
print("3\ Black Jack")
lista_cartas = list(cartas) #para que me cree una lista de mi lista

print("Ha seleccionado:", end=" ") #end para que cierre el diccionario, para que solo pueda seleccionar 1 carta
carta = choice(lista_cartas) #choice de la carta que he seleccionado de la lista de cartas
score = cartas[carta] #score para saber el valor de la carta que me ha dicho de la lista de las cartas
print(carta, end=" ") 
carta = choice(lista_cartas)
score += cartas[carta] #sumar al anterior cartas[carta] el siguiente
print(carta, end=" ")
print(" >>> su puntuación es de", score)

main_banca = sample(lista_cartas, 2) #el sample baraja
score_banca = sum(cartas[carta] for carta in main_banca)
print("La banca tiene: {} {}  >> su score es {}".format(main_banca[0],
                                                          main_banca[1],
                                                          score_banca))