inventory = {} #Dictionary to store inventory data

#Display menu
def display_menu():
    print("Please choose an operation:-")
    print("1-Add or Update item\n2-Get item quantity\n3-List inventory\n4-Exit")

#Add or Update inventory
def add_or_update_item(item_name , quantity):
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity

#Get item quantity
def get_item_quantity(item_name):
    if item_name in inventory:
        return inventory[item_name]
    else:
        return 0

#List inventory
def list_inventory():
    z = 1
    for i in inventory.keys():
        print(f"{z}.{i} = {inventory[i]}")
        z += 1

#User input
def get_user_input():
    return input("Enter your choice: ")

#Main
print("Welcome to the inventory data system!!")
while True:

    display_menu()
    user_choice = get_user_input()
    user_choice.lower()

    if user_choice == "1" or user_choice == "add or update item":
        item = input("Enter the item name: ")
        item = item.lower()
        item_quantity = int(input("Enter the item quantity: "))
        add_or_update_item(item , item_quantity)
    if user_choice == "2" or user_choice == "get item quantity":
        item = input("Enter the item name: ")
        print(get_item_quantity(item))
    if user_choice == "3" or user_choice == "list inventory":
        list_inventory()
    if user_choice == "4" or user_choice == "exit":
        break