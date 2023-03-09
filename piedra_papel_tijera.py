jugador1 = input("Ingresa la jugada del jugador uno: piedra, papel o tijera ")
jugador2 = input("Ingresa la jugada del jugador dos: piedra, papel o tijera ")

if jugador1 == "piedra" and jugador2 == "piedra":
    print("Es empate")
if jugador1 == "piedra" and jugador2 == "papel":
    print("Gane el jugador 2")
if jugador1 == "piedra" and jugador2 == "tijera":
    print("Gana el jugador 1")
if jugador1 == "papel" and jugador2 == "piedra":
    print("Gana el jugador 1")
if jugador1 == "papel" and jugador2 == "papel":
    print("Es empate")
if jugador1 == "papel" and jugador2 == "tijera":
    print("Gana jugador 2")
if jugador1 == "tijera" and jugador2 == "piedra":
    print("Gana el jugador 2")
if jugador1 == "tijera" and jugador2 == "papel":
    print("Gana el jugador 1")
if jugador1 == "tijera" and jugador2 == "tijera":
    print("Es empate")
