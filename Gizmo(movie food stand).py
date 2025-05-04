# concession stand

manu ={"kota":"25.00",
       "Fat cakes":"2.00",
       "cola": "10.00",
       "fanta": "15.00",
       "candy":"0.55"}


cart=[]
total=0


print("----------Manu--------")
for key, value in manu.items():
    print(f"{key:50}:R{value}")
print("----------Manu--------")

while True:
    food=input("Select an item (q to quit):").lower()
    if food=="q":
        break
    elif manu.get(food) is not None:
        cart.append(food)

print("------Your order------")
for food in cart:
    total =total+ float(manu.get(food))
    print(food, end=" ")

print()
print(f"total is:{total}")




print(cart)












