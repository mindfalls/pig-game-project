import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll
comp_score = 0
player_score = 0
def comp_turn():
    global comp_score
    max_score = 50
    current_score = 0
    while comp_score < max_score:
        value = roll()
        if  current_score > 18:
            comp_score += current_score
            print("comp score is",comp_score)
            player_turn()
        elif value > 1:
            print("comp rolled:", value)
            current_score += value
        elif value == 1:
            print("comp rolled 1! Your turn")
            current_score += 0
            player_turn()
    if comp_score > max_score:
        print("comp wins!")
        exit()
    

def player_turn():
    
    global player_score
    max_score = 50
    current_score = 0
    while player_score < max_score:
        should_roll = input("Would you like to roll (y)? ")
        if should_roll.lower() == "y" :
            
            value = roll()
            if value > 1 :
                print("You rolled a: ", value)
                current_score += value
                print("Your score is:" , current_score)
            else:
                print("you rolled a 1! Turn done")
                current_score = 0
                comp_turn()
        else:
            player_score += current_score
            print("player_score:" , player_score)
            comp_turn()
    if player_score > max_score:
        print("congrats! You won")
        exit()
            
comp_turn()