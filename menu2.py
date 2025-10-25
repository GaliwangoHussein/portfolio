menu = {"rolex": 2000,
       "chips": 10000,
       "soda": 5000,
       "chicken": 15000,
       "pilau": 12000,
       "beef": 18000,
       "katogo": 8000,
       "fish": 10000} 

print("Welcome to the Restaurant!")
print("Menu:")
for item, price in menu.items():
    print(f"{item}. ugx {price}")
    
choice = input("please enter the item you want to order: ")
if choice in menu:
    price = menu[choice]
    print(f"You ordered: {choice}. Price: ugx {price}")
    

