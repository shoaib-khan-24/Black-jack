import random
from art import logo

card_deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def black_jack(y_score, c_score):
    if y_score > 21:
        print("You crossed the limit. *BURST* ")
        print("You lose.")
        return
    elif y_score == 21:
        print("Black-jack. ** You Win **")
        return
    elif c_score > 21:
        print("Computer crossed the limit. *BURST* ")
        print("You win 😁")
        return
    elif c_score == 21:
        print("Computer black-jacked. ** You lose 😭 **")
        return
    choice = input("press 'y' for hit or 'n' for stand\n").lower()
    if choice == 'n':
        if 21-y_score < 21-c_score:
            print("You win 😁")
            print(f"your score = {y_score} and computer score = {c_score} with computer's last card = {computer_score_list[-1]}")
        elif 21-y_score > 21-c_score:
            print("You lose 😭")
            print(f"your score = {y_score} and computer score = {c_score} with computer's last card = {computer_score_list[-1]}")
        else:
            print("Draw 😶")
            print(f"your score = {y_score} and computer score = {c_score} with computer's last card = {computer_score_list[-1]}")
    elif choice == 'y':
        your_score_list.append(random.choice(card_deck))
        y_score += your_score_list[-1]
        if your_score_list[-1]==11 and y_score>21:
            your_score_list[-1] = 1
            y_score -= 10
        print(f"you status : your cards = {your_score_list}  your score = {y_score}")

        black_jack(y_score, c_score)

#
# if play_game == 'y':
#
# elif play_game == 'n':
#     print("Exit the game.")
# else:
#     print("Invalid input. Go to hell.")

play_game = "y"
while play_game == 'y':
    print(logo)
    computer_score = 0
    computer_score_list = [10]
    computer_score += computer_score_list[-1]

    your_score_list = []
    your_score = 0

    your_score_list.append(random.choice(card_deck))
    your_score += your_score_list[-1]
    your_score_list.append(random.choice(card_deck))
    your_score += your_score_list[-1]
    print(f"you status : your cards = {your_score_list}  your score = {your_score}")
    print(f"computer status : computer cards = {computer_score_list} computer score = {computer_score}")
    while computer_score < 17:
        computer_score_list.append(random.choice(card_deck))
        computer_score += computer_score_list[-1]
    black_jack(your_score, computer_score)
    play_game = input("Do you want to play blackjack game ? y/n :  ").lower()

print("Exited the game.")

