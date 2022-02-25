from unicodedata import name


likedIngredients = []

peopleCOunt = int(input("Enter people count"))
likeIngCount = int(input("Enter like ing count"))
for i in range(likeIngCount):
    ingName = input("Enter ingredient")
    if len(likedIngredients) != 0:
        for j in likedIngredients:
            if j["name"] == ingName:
                j["rating"] = j["rating"] + 1
            else :
                likedIngredients.append({
                        "name": ingName,
                        "rating": 1
                })
    else:
        likedIngredients.append({
                        "name": ingName,
                        "rating": 1
        })
dislikeIngCount = int(input("Enter dis like ing count"))
for i in range(dislikeIngCount):
    ingName = input("Enter ingredient")
    if len(likedIngredients) != 0:
        for j in likedIngredients:
            if j["name"] == ingName:
                j["rating"] = j["rating"] - 1
            else :
                likedIngredients.append({
                        "name": ingName,
                        "rating": -1
                })
    else:
        likedIngredients.append({
                        "name": ingName,
                        "rating": -1
        }) 

print("text")
print(len(likedIngredients))

for i in likedIngredients:
    print("111")
    print(i)