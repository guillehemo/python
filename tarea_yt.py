class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    
     def atributos(self):
        print(self.nombre, ":", sep="")
        print("Fuerza", self.fuerza)
        print("Inteligencia", self.inteligencia)
        print("Defensa", self.defensa)
        print("Vida", self.vida)

mi_personaje = Personaje("BitBoss", 10, 1, 5, 100)
mi_personaje.atributos()