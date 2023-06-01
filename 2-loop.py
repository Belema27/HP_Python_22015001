for b in range(1, 101):
    if b % 3 == 0 and b % 5 == 0:
        print("couples", end=", ")
    elif b % 3 == 0:
        print("boys", end=", ")
    elif b % 5 == 0:
        print("girls", end=", ")
    else:
        print(b, end=", ")
