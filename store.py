player = {"name": "Orenday", "gold": 100, "inventory": []}
shop = {"potion": 30, "sword": 80, "shield": 60}

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
        print("LOAD MATCH")
        return {"name": "Orenday", "gold": gold, "inventory": inventory_list}
    except (FileNotFoundError, ValueError, IndexError):
        print("NEW MATCH")
        return {"name": "Orenday", "gold": 100, "inventory": []}

def save_game(player):
    with open("save.txt", "w") as save:
        inventory = ", ".join(player["inventory"])
        save.write(f"GOLD: {player['gold']}\nInventory: {inventory}")

def buy(player, item):
    if item in shop:
        price = shop[item]
        if player["gold"] >= price:
            player["gold"] = player["gold"] - price
            player["inventory"].append(item)
            print(f"You bought {item}")
        else:
            print(f"Not enough gold. {item} costs {price} and you have {player['gold']}")
    else:
        print(f"{item} does not exist in the shop")

def sell(player, item):
    if item in player["inventory"]:
        price = shop[item]
        player["gold"] = player["gold"] + (price//2)
        player["inventory"].remove(item)
        print(f"You sold {item}")
    else:
        print(f"You dont have {item}")
        

player = load_game()

while True:
    option = input("BUY | INVENTORY | GOLD | SHOP | SELL | EXIT : ").lower()
    if option == "buy":
        item = input("Which item SWORD | POTION | SHIELD :").lower()
        buy(player, item)
    elif option == "inventory":
        print(player["inventory"])
    elif option == "gold":
        print(f"You have {player['gold']} gold")
    elif option == "shop":
        for item_name, price in shop.items():
            print(f"{item_name}: {price}")
    elif option == "sell":
        item = input(f"which item {player['inventory']} do you want to sell? ").lower()
        sell(player, item)
    elif option == "exit":
        save_game(player)
        print("EXIT TO THE GAME")
        break
    else:
        print("Invalid option")
