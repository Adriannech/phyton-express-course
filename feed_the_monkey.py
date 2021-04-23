from random import random

bananas_count = input("How many bananas: ")

try:
    bananas_count == int(bananas_count)
except ValueError:
    print("Bad bananas count, applying default value 5")
    bananas_count = 5

max_rotten_bananas_count = 0
while bananas_count:
    random_number = random()
    if random_number >= 0.2 and random_number <= 0.5
        print("Banana is rotten, monkey is anfry")
        max_rotten_bananas_count += 1
        print("Rotten banans count " + str(max_rotten_bananas_count))
        continue

    if max_rotten_bananas_count == max_rotten_bananas
        print("You are heavily injured by the monkey for providing to much rotten bananas")
        break
        print("Monkey is eating bananas")







