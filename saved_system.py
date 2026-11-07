def load_game():
    try:
        with open("save.txt", "r") as save:
            lines = save.readlines()
            gold = int(lines[0].split(": ")[1])
            inventory_text = lines[1].split(": ")[1].strip()
            if inventory_text:
                inventory_list = inventory_text.split(", ")
            else:
                inventory_list = []
        print("LOAD GAME")
        return {"name": "Orenday", "gold": gold, "inventory": inventory_list}
    except (FileNotFoundError, ValueError, IndexError):
        print("NEW GAME")
        return {"name": "Orenday", "gold": 100, "inventory": []}

def save_game(player):
    with open("save.txt", "w") as save:
        inventory = ", ".join(player["inventory"])
        save.write(f"GOLD: {player['gold']}\nInventory: {inventory}")
