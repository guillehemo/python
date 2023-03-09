palabra = input("Ingresa una palabra: ")

while palabra != "chupacabra":
    palabra = input("Palabra incorrecta, por favor ingresa otra palabra: ")
    if palabra == "chupacabra":
        break
print("¡Has dejado el bucle con éxito.")