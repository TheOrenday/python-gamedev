import random
player_name = "Luffy"
health = 100
damage = 35
is_alive = True
enemy = "Smoke"
health_enemy = 100
damage_enemy = 35
boss = True
health = health - damage_enemy
print(player_name)
print(health)
print(damage)
print(is_alive)
print(enemy)
print(health_enemy)
print(damage_enemy)
print(boss)

print(type(player_name))
print(type(health))
print(type(damage))
print(type(enemy))
print(type(health_enemy))
print(type(damage_enemy))
print(type(boss))

name = input("Enter your hero's name: ")
print(f"Bienvenid {name}")
level = int(input("Enter your level: "))
health_from_level = level * 20
enemy_xp = 35 
enemy_defeated =int(input("cuantos enemigos derrotaste: "))
enemy_xp = enemy_xp * enemy_defeated
monedas = 47
monedas = 47 % 5
print(monedas)
print(enemy_xp)

helath_exercise3 = 30
if helath_exercise3 <= 0:
    print("Game over")
elif helath_exercise3 < 15:
    print("Warning: low health")
else:
    print("You are doing fine")


health_player = int(input("Cual es tu vida:"))
if health_player <= 0:
    print("Game Over")
elif health_player < 20:
    print("Vida critica")
elif health_player < 60:
    print("Herido")
else:
    print("Vida sana")

opciones = ["piedra", "papel", "tijeras"]
jugador = input("¿Elige piedra papel o tijera:")
computadora = random.choice(opciones)
print(f"La computadora eligio {computadora}")
if jugador == computadora:
    print ("empate")
elif (
    (jugador == "piedra" and computadora == "tijeras")
    or (jugador == "papel" and computadora == "piedra")
    or (jugador == "tijeras" and computadora == "papel")):
    print ("Ganaste")
else: 
    print("perdiste la computadora gano")

print("Bienvenido al juego de llaves")
jugador_llave = (input("Tienes la llave si/no: "))
nivel = int(input("Que nivel eres: "))
if jugador_llave == "si" and nivel >= 5:
    print("Abres la puerta")
elif jugador_llave == "si" and nivel < 5:
    print("tienes la llave, pero no el nivel")
elif jugador_llave == "no" and nivel >= 5:
    print("Tiees el nivel pero no la llave")
else:
    print("No tienes el nivel ni la llave")

vidaenemigo = 100
jugadordaño = 12
while vidaenemigo >= 0:
    vidaenemigo = vidaenemigo - jugadordaño
    print(f"DAÑO la vida del enemigo ahora es de: {vidaenemigo}")

for i in range(1, 11):
    xp_necsario = i * 100
    print(f"El nivel {i} necesita {xp_necsario} ")


vida = 100
malo = 100
daño = 30
curacion = 50

while True:
    option = input("Que quieres hacer atacar, curar o salir: ").lower()
    if malo <= 0:
        malo = 0
        print("Ganaste")
    if option == "atacar":
        malo = malo - daño
        print(f"Atacaste al malo y quitaste {daño} de vida. Al malo le quedan {malo} vida")
    elif option == "curar":
        vida = vida + curacion
        print(f"Tu curaste {curacion} de vida")
    elif option == "salir":
        print("Slaiste del juego")
        break
    else: 
        print("Opcion no valida ")