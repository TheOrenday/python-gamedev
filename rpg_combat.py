import random
hero = {"name": "Luffy", "health": 100, "damage": 25}
enemy = {"name": "Smoke", "health": 80, "damage": 20}

def attack(target, damage):
    target["health"] = max(0, target["health"] - damage)

def heal(character, amount):
    character["health"] = min(100, character["health"] + amount)

def show_status(hero, enemy):
    print(f"La vida de {hero['name']} es de {hero['health']}")
    print(f"La vida de {enemy['name']} es de {enemy['health']}")

def roll_damage(base):
    return random.randint(base -5, base + 5)
while True:
    show_status(hero, enemy)
    option = input("¿Que haces? atacar | curar | huir : ").lower()
    if option == "atacar":
        damage = roll_damage(hero["damage"])
        critico = random.randint(1, 5)
        if critico == 1:
            damage = damage * 2
            print("GOLPE CRITICO")
        attack(enemy, damage)
        print(f"Atacaste y quitaste {damage} de vida")
    elif option == "curar":
        heal_amount = 20
        before = hero["health"]
        heal(hero, heal_amount)
        recovered = hero["health"] - before
        print(f"Te curaste {heal_amount} de vida")
    elif option == "huir":
        print("Saliste del combate")
        break
    else:
        print("Opcion no valida")
        continue
    if enemy["health"] <= 0:
        print("Ganaste")
        break

    enemy_damage = roll_damage(enemy["damage"])
    critico_enemy = random.randint(1, 10)
    if critico_enemy == 1:
        enemy_damage = enemy_damage * 2
        print("El enemigo te ha dado un golpe critico")
    attack(hero, enemy_damage)
    print(f"{enemy['name']} te contrataco y te quito {enemy_damage} de vida")
    
    if hero["health"] <= 0:
        print("Perdiste")
        break

