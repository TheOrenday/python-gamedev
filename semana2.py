inventory = ["sombrero", "espada", "resortera"]


inventory.append("cigarro")
inventory.append("mapa")
inventory.remove("resortera")

print(len(inventory))
for item in inventory:
    print(f"tu tienes: {item}")

option = input("Que item buscas? ")
print(option in inventory)

record = [2000, 3000, 4500, 2275, 4499, 7000]
record.sort(reverse=True)
print(record[:3])

import random
loot = ["diamante", "esmeralda", "plata", "oro", "carbon"]
for i in range(5):
    soltar = random.choice(loot)
    print(f"El enemigo ha soltado {soltar}")

mochila = []
while True:
    option = input("Que deseas hacer agregar / quitar / ver / salir : ").lower()
    len(mochila)
    if option == "agregar":
        if len(mochila) >= 5:
            print("Tu mochila esta llena")
        else:
            item = input("Que item agregas?")
            mochila.append(item)
            print(f"Se agrego {item} a tu mochila ")
    elif option == "quitar":
        item = input("Que item quitas?")
        if item in mochila:
            mochila.remove(item)
            print(f"Quitaste {item}")
        else:
            print("Ese item no esta en tu mochila")
    elif option == "ver":
        print(f"Tu mochila: {mochila}")
    elif option == "salir":
        print("Saliste del juego")
        break
    else:
        print("Opcion no valida")

player = {
    "nombre": "Luffy",
    "vida": 100,
    "arma": "puños",
    "nivel": 10
}
for clave, valor in player.items():
    print(f"{clave}: {valor}")

weapon = {
    "pocion": 2,
    "balas": 60,
    "flechas": 20
}
while True:
    opcion = input("Que item deseas usar pocion, balas, flechas, salir : ").lower()
    if opcion == "salir":
        break
    elif opcion in weapon:
        if weapon[opcion] > 0:
            weapon[opcion] = weapon[opcion] - 1
            print (f"Ahora tienes {weapon[opcion]} {opcion}")
        else:
            print(f"Ya no te quedan {opcion}")
    else:
        print("Ese item no existe")
for clave, valor in weapon.items():
    print(f"{clave}: {valor}")

valores = {
    "vida": 100,
    "malo": 100,
    "atacar": 30,
    "curar": 50
}

while True:
    option = input("Que quieres hacer atacar, curar o salir: ").lower()
    if option == "atacar":
        max(0, valores["malo"])
        valores["malo"] = valores["malo"] - valores["atacar"]
        print(f"Atacaste al malo y quitaste {valores['atacar']} de vida. Al malo le quedan {valores['malo']} vida")
        if valores["malo"] <= 0:
            print("Ganaste")
            break
    elif option == "curar":
        min(100, valores["vida"])
        valores["vida"] = valores["vida"] + valores["curar"]
        print(f"Tu curaste {valores['curar']} de vida, tu vida ahora es de {valores['vida']}")
    elif option == "salir":
        print("Saliste del juego")
        break
    else: 
        print("Opcion no valida ")

def is_alive(health):
    return health > 0

health = 100
print(f"Esta vivo: {is_alive(health)}")

health = 0 
print(f"Esta vivo: {is_alive(health)}")

def heal(health, amount):
    return min(100, health + amount)

health = 70
health = heal(health, 20)     # debería dar 90
print(health)

health = heal(health, 50)     # debería dar 100, no 140
print(health)