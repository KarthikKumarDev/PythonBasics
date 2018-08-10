import random

health_points = 50

difficulty = 1

potion_value = int(random.randint(25, 100) / difficulty)

health_points += potion_value

print(potion_value)

print(health_points)