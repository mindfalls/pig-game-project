import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


def comp_play():
    value = roll()
    current_score = 0
    max_score = 50
    while current_score < max_score :
        roll()
        if value == 1:
            print("1 was rolled")
            current_score = 0
            break
        else:
            print("comp rolled a", value)
            current_score += value
    return current_score

print(comp_play())