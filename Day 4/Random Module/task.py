import random

# random.randint
#rand_int = random.randint(1, 10)
#print(rand_int)

# random.randint
#rand_num_0_to_1 = random.random() * 10
#print(rand_num_0_to_1)

# random.uniform
#rand_float = random.uniform(1, 10)
#print(rand_float)

# GAME: HEADS OR TAILS
coin_flip = random.randint(0, 1)
if coin_flip == 0:
    print("Heads")
elif coin_flip == 1:
    print("Tails")
else:
    print("How tf?")

# HOW TO IMPORT MY OWN MODULE
#import my_module
#print(my_module.my_fav_num)