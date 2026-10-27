import random
heroe = {"nombre": "Luffy", "vida": 100, "daño": 25}
enemigo = {"nombre": "Crocodile", "vida": 85, "daño": 20}

def atacar(jugador, daño):
    jugador["vida"] = max(0, jugador["vida"] - daño)

def curar(jugador, cantidad):
    jugador["vida"] = min(100, jugador["vida"] + cantidad)

def estatus(heroe, enemigo):
    print(f"La vida de {heroe['nombre']} es de {heroe['vida']}")
    print(f"La vida de {enemigo['nombre']} es de {enemigo['vida']}")

def rol_daño(base):
    return random.randint(base -5, base + 5)

while True:
    estatus(heroe, enemigo)
    opcion = input("QUE DESEAS HACER ATACAR | CURAR | HUIR : ").lower()
    if opcion == "atacar":
        daño = rol_daño(heroe["daño"])
        daño_critico = random.randint(1, 5)
        if daño_critico == 1:
            daño = daño * 2
            print("GOLPE CRITICO")
        atacar(enemigo, daño)
        print(f"Atacaste y quitas {daño} de vida a {enemigo['nombre']} ")
    elif opcion == "curar":
        cantidad = 20
        antes = heroe["vida"]
        curar(heroe, cantidad)
        vida_recuperada = heroe["vida"] - antes
        print(f"Te curaste {vida_recuperada} de vida")
    elif opcion == "huir":
        print("SALISTE DEL COMBATE")
        break
    else:
        print("OPCION NO VALIDA")
        continue
    if enemigo["vida"] <= 0:
        print("GANASTE")
        break
    enemigo_daño = rol_daño(enemigo["daño"])
    daño_critico_enemigo = random.randint(1, 10)
    if daño_critico_enemigo == 1:
        enemigo_daño = enemigo_daño * 2
        print("GOLPE CRITICO DEL ENEMIGO")
    atacar(heroe, enemigo_daño)
    print(f"{enemigo['nombre']} te contrataco y le quito {enemigo_daño} de vida a {heroe['nombre']} ")
    if heroe["vida"] <= 0:
        print("PERDISTE")
        break