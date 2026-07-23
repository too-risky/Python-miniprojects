#Cart

foods = []
prices = []
total = 0

while True :
    food = input("Enter food item (q to quit) : ")
    if food.lower() == "q" :
        break
    else :
        foods.append(food)
        price = float(input("Enter the price of the item : $ "))
        prices.append(price)

print()
print("~~~~YOUR CART~~~~")
print()
print(foods)
for price in prices :
    total += price

print()
print(f"Your total is : ${total}")