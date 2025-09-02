Favourite_food=["Pizza", "Burger", "Pasta", "Sushi"]
for i in range(len(Favourite_food)):
    if "Burger" in Favourite_food:
        index1= Favourite_food.index("Burger")
        Favourite_food.remove("Burger")
        Favourite_food.insert(index1, "Cheeseburger")
        break
print(Favourite_food)