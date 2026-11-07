shop = {"potion": 30, "sword": 80, "shield": 60}
sell_prices = {"potion":shop["potion"]//2, "sword":shop["sword"] *3//4, "shield":shop["shield"]//2}
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
        price = sell_prices[item]
        player["gold"] = player["gold"] + price
        player["inventory"].remove(item)
        print(f"You sold {item}")
    else:
        print(f"You don't have {item}")