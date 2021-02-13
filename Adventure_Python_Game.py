import time
import random

items = []
people = ["Adolf Hitler", "Benito Musoline", "King Leopold", "Alexander Hamilton"]
enemy = random.choice(people)


def print_pause(message):
    '''prints out messages slowly'''
    time.sleep(1)
    print(message)
    time.sleep(1)


def intro():
    '''Describes the world to player'''
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that the wicked " + enemy +
                " is somewhere around here, and has been terrifying"
                " the nearby village.\n")


def landing():
    '''Where the player starts the world'''
    print_pause("Enter 1 to knock on the door of the house.\n"
                "Enter 2 to peer into the cave. \n"
                "What would you like to do?")
    option = valid_input("Please enter 1 or 2\n", ['1', '2'])
    if option == '1':
        house()
    elif option == '2':
        cave()


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause("Sorry, I don't understand " + option + ".")


def house():
    '''What happens inside house'''
    print_pause("You approach the door of the house")
    print_pause("You are about to knock when the door opens"
                " and out steps " + enemy)
    print_pause("Eep! This is the enemy's house!")
    print_pause(enemy + " attacks you!")
    fight()


def fight():
    '''Player fights'''
    if 'sword' not in items:
        print_pause("You feel a bit under-prepared for this,"
                    " what with only having a tiny dagger")
        action = valid_input("Would you like to 1 fight, or 2 run away?\n",
                             ['1', '2'])
        if action == '2':
            print_pause("You run back into the field. "
                        "Luckily, you don't seem to have been followed.")
            landing()
        else:
            print_pause("You do your best...")
            print_pause("but your dagger is no match for " + enemy)
            print_pause("you have been defeated!")
            restart_game()
    else:
        action = valid_input("Would you like to 1 fight, or 2 run away?\n",
                             ['1', '2'])
        if action == '2':
            print_pause("You run back into the field."
                        "Luckily, you don't seem to have been followed.")
            landing()
        else:
            print_pause("As " + enemy + " moves to attack,"
                        " you unsheath your new sword.")
            print_pause("The Sword of Ogoroth shines brightly"
                        " in your hand")
            print_pause("as you brace yourself for the attack.")
            print_pause("But " + enemy + " takes one look "
                        "at your shiny new toy and runs away!")
            print_pause("You have rid the town of " + enemy)
            print_pause("\nYOU ARE VICTORIOUS\n")
            restart_game()


def cave():
    '''Cave'''
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Sword of Ogoroth!")
    print_pause("You discard your silly old dagger and"
                " take the sword with you.")
    print_pause("You walk back out to the field.\n")
    items.append("sword")
    landing()


def restart_game():
    '''Play again?'''
    print_pause("\n\nGAME OVER\n")
    again = valid_input("\nWould you like to play again?\n"
                        "Enter 'yes' or 'no'\n", ["yes", "no"])
    if "yes" in again:
        print_pause("\nExcellent! Restarting the game...\n\n")
        play_game()
    elif "no" in again:
        print_pause("\nGoodbye, brave warrior")


def play_game():
    intro()
    landing()


play_game()
