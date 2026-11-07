wizard = {"name": "Merlin", "mana": 50, "spell": []}
spell_cost = {"fireball": 30, "heal": 20, "shield": 15}

player = {"vida": 100}
amount = 20
def heal(player, amount):
    player["vida"] = min(100, player["vida"] + amount)
    return(player["vida"])

new_heal = heal(player, amount)
print(f"Nueva vida {new_heal}")

def learn(wizard, spell):
    if spell in spell_cost:
        if spell not in wizard["spell"]:
            wizard["spell"].append(spell)
            print(f"You lernaed spell {spell}")
        else:
            print("YOU KNOW")
    else:
        print("NO EXIST")

def cast(wizard, spell):
    if spell in wizard["spell"]:
        price = spell_cost[spell]
        if wizard["mana"] >= price:
            wizard["mana"] = wizard["mana"] - price
            print(f"You use spell {spell}")
        else:
            print(f"Your mana is not sufficiente, you have {wizard["mana"]} is mana")
    else:
        print(f"You don't know {spell}")

while True:
    option = input("Que quieres elegir APRENDER | USAR | HECHIZOS | MANA | SALIR : ").lower()
    if option == "aprender":
        spell = input("Que habilidad FIREBALL | HEAL | SHIELD : ").lower()
        learn(wizard, spell)
    elif option == "usar":
        spell = input(f"Cual hechizo quieres usar {wizard['spell']} ").lower()
        cast(wizard, spell)
    elif option == "hechizos":
        print(f"Tus hechizos son {wizard["spell"]}")
    elif option == "mana":
        print(f"Tienes actualamete {wizard['mana']} de mana")
    elif option == "salir":
        print("Saliste del juego")
        break
    else:
        print("opcion no valida")
