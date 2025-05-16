menu = {"pizza":200,"burger":50,"spring roll":20,"coldrink":20,"chhole bathure":100,"pao bhaji":50,"samosa":10,
        "bedai/kachodi":10}

cart = []
total = 0

print("------- MENU ---------")
for key, value in menu.items():
    print(f"{key:15}: Rs.{value:.2f}")

print("---------------------------")

while True:
    food = input("Select an item or (q for quite):").lower()
    if food.lower() =="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print(f"Selected {food} item is not available")
print()
print("------YOUR ORDER--------")
for food in cart:
    total += menu.get(food)
    print(food,end=" ")

print()
print(f"Your Total is: Rs.{total:.2f}")
print("--------xxxxx---------")