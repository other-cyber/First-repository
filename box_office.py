ages = [15,8,18,12,9]
movie_rating = "PG-13"
is_weekend = True
friends = ["Кирилл", "Леша", "Ваня", "Вова", "Саша"]
can_watch = True
a = ""
if len(ages) == 0 or len(friends) == 0:
    print("Нет друзей")
else:
    if movie_rating == "G":
        can_watch = True
    elif movie_rating == "PG":
        for i in range(len(ages)):
            if ages[i] <= 8:
                a += friends[i] + ", "
                can_watch = False
    elif movie_rating == "PG-13":
        for i in range(len(ages)):
            if ages[i] < 13:
                a += friends[i] + ", "
                can_watch = False
    elif movie_rating == "R":
        for i in range(len(ages)):
            if ages[i] <= 17:
                a += friends[i] + ", "
                can_watch = False
    if is_weekend and can_watch:
        print("Проходят все")
        print(f"Цена: {12 * len(friends)}")
    elif can_watch == True:
        print("Проходят все")
        print(f"Цена: {10 * len(friends)}")
    else:
        print("Не проходят: " + a[:-2])