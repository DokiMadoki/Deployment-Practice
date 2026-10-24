import json

def calculate_total(chosen_dishes, menu):
    total_price = 0
    for items in chosen_dishes:
        total_price = total_price + menu[items]
          
    return (total_price)
with open("menu.json") as f:
    menu = json.load(f)
while True:
    try:
        guests = int(input("How many guests need to be served?"))
        break
    except ValueError:
        print("Please enter a number!")
chosen_dishes = [] 
while True:
    choice = input("What Dish do you want?")

    if choice == "done":
        break

    elif choice.title() in menu:
        chosen_dishes.append(choice.title())
        print("Added to Menu")

    else:
        print("Item is not in menu") 





per_plate_price = calculate_total(chosen_dishes, menu)
cost = per_plate_price * guests
discount = False
if guests > 500:
    discount = True
    cost = cost * 0.9

print(f"The per plate price is {per_plate_price}")
print(f"The menu items are")
for items in chosen_dishes:
    print(items)

if discount:
    print(f"Discount of 10% applied")
print(f"The Total Cost for serving {guests} Guests is {cost}")
quote = {"price_per_plate": per_plate_price, "menu": chosen_dishes, "guests": guests, "discount": discount,"total_price": cost}
try:
    with open("quotes.json") as f:
        quotes = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    quotes = []

quotes.append(quote)
with open("quotes.json", "w") as f:
    json.dump(quotes, f, indent=2)