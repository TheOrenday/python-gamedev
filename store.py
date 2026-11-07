from buy_and_sell import buy, sell, shop
from saved_system import load_game, save_game
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
        item = input(f"Which item {player['inventory']} do you want to sell? ").lower()
        sell(player, item)
    elif option == "exit":
        save_game(player)
        print("GAME SAVED")
        break
    else:
        print("Invalid option")
