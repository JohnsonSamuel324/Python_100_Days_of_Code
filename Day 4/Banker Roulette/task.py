import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#1
print(random.choice(friends))

#2
rand_int = random.randint(0, len(friends) - 1)
print(friends[rand_int])