import random


def roll():

    """
    Returns a number between 1-6
    """
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


comp_score = 0
player_score = 0


def comp_turn():

    """
    Function for simple computer behaviour
    """
    global comp_score
    global player_score
    max_score = 50
    current_score = 0
    print("comp turn has begun!\n")
    while comp_score < max_score:
        value = roll()
        if current_score > 18:
            comp_score += current_score
            print("comp score is", comp_score)
            player_turn()
        elif value > 1:
            print("comp rolled:", value)
            current_score += value
        elif value == 1:
            print("comp rolled 1! Your turn")
            current_score += 0
            player_turn()
    if comp_score >= max_score:
        print("comp wins!")
        comp_score = 0
        player_score = 0
        play_again()


def player_turn():
    """
    Function for player turn when playing against cpu
    """

    global player_score
    global comp_score
    max_score = 50
    current_score = 0
    print("Player turn has begun!\n")
    print("Your Score is: ", player_score)
    while player_score < max_score:
        should_roll = input("Would you like to roll (y)? \n")
        if should_roll.lower() == "y":

            value = roll()
            if value > 1:
                print("You rolled a: ", value)
                current_score += value
                print("Your score is:", current_score)
            else:
                print("you rolled a 1! Turn done")
                current_score = 0
                comp_turn()
        else:
            player_score += current_score
            print("player_score:", player_score)
            comp_turn()
    if player_score >= max_score:
        print("congrats! You won")
        player_score = 0
        comp_score = 0
        play_again()


def rules():
    """
    Displays rules for user if user so wishes
    """
    while True:
        know_rules = input("Would you like to know the rules? (y)\n")
        if know_rules.lower() == "y":
            print("Rules of Pig are simple. A player rolls for a number.")
            print("If the number rolled is 1, the turn ends")
            print("If the number rolled is from 2-6.")
            print("Player adds to score and decides to roll again or not")
            print("If player decides to stop, player keeps the current score")
            print("First player to reach 50 points wins")
            break
        elif know_rules.lower() == "n":
            break

        else:
            print("Invalid, try again.")


def game():
    """
    Lets user choose how many players and also lets user play game
    """
    while True:
        players = input("Enter the number of players (1 - 4):\n ")
        if players.isdigit():
            players = int(players)
            if 2 <= players <= 4:
                break
            elif players == 1:
                comp_turn()
                break
            else:
                print("Must be between 2 - 4 players.")
        else:
            print("Invalid, try again.")

    max_score = 50
    player_scores = [0 for _ in range(players)]

    while max(player_scores) < max_score:
        for player_idx in range(players):
            print("\nPlayer number", player_idx + 1, "turn has just started!")
            print("Your total score is:", player_scores[player_idx], "\n")
            current_score = 0

            while True:
                should_roll = input("Would you like to roll (y)? \n")
                if should_roll.lower() != "y":
                    break

                value = roll()
                if value == 1:
                    print("You rolled a 1! Turn done!\n")
                    current_score = 0
                    break
                else:
                    current_score += value
                    print("You rolled a:", value)

                print("Your score is:", current_score)

            player_scores[player_idx] += current_score
            print("Your total score is:", player_scores[player_idx])

    max_score = max(player_scores)
    winning_idx = player_scores.index(max_score)
    print("Player number", winning_idx + 1,
          "is the winner with a score of:", max_score)


def play_again():
    """
    User can choose to play game once more
    """
    while True:
        play_again = input("Would you like to play again?(y) or (n) ")
        if play_again.lower() == "y":
            game()
        elif play_again.lower() == "n":
            exit()
        else:
            print("Invalid, try again.")


def main():
    print("Welcome to Pig game!")
    rules()
    game()
    while True:
        play_again()


main()
