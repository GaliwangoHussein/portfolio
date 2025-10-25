# Simple restaurant menu program

menu = {
    "1": ("Burger", 250),
    "2": ("Pizza", 500),
    "3": ("Fries", 150),
    "4": ("Drink", 100)
}

print("Welcome to the Restaurant!")
print("Menu:")
for key, (item, price) in menu.items():
    print(f"{key}. {item} - Rs {price}")

choice = input("Please enter the number of the item you want to order: ")

if choice in menu:
    item, price = menu[choice]
    print(f"You ordered: {item}. Price: Rs {price}")
else:
    print("Invalid choice. Please try again.")