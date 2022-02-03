import time
import random
import enum


class Color(enum.Enum):
    red = '\033[91m'
    purple = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    black = '\033[0m'

    @classmethod
    def get_color(cls):
        return random.choice([color.value for color in cls])


weapons_list = ["sword", "dagger", "axe", "katana", "lance"]
bad_men_list = ["kidnappers", "ritualists", "terrorists",
                "rapists", "cultists"]


def print_pause(message, delay=0):
    print(Color.get_color() + message)
    time.sleep(delay)


def intro():
    print_pause("You return from shopping at the mall to "
                "find your mum wailing.", 3)
    print_pause("Upon inquiry, you are told that your "
                "younger sister has been taken away by "
                f"{bad_men}.", 3)
    print_pause("You ask the neighbors who are consoling "
                "your mother which direction they went and "
                "they point to a path close to your house.", 3)
    print_pause("You run towards that direction before your "
                "mum can stop you.", 3)
    print_pause("Soon enough, you come to a place where the "
                "road splits into two.", 3)
    print_pause("The one to your right looks dark but "
                "wide.", 3)
    print_pause("The one to your left looks bright but "
                "narrow.", 3)
    print_pause("To go right, enter 1.")
    print_pause("To go left, enter 2.")


def valid_input(message, options):
    while True:
        option = input(message).lower()
        if option in options:
            return option
        print_pause(f'Sorry, the option "{option}" is '
                    'invalid. Try again!')


def fight(weapons_holder,):
    print_pause(f"You fight with the {bad_men}.", 1)
    if weapons in weapons_holder:
        print_pause(f"The {bad_men} move to attack "
                    f"you, you draw your shiny {weapons} "
                    "and fight fiercely with them.", 1)
        print_pause("You defeat them with your "
                    f"{weapons}.", 1)
        print_pause("You've won!", 1)
        print_pause("You untie your sister and go "
                    "home with your head held high.", 1)
    else:
        print_pause("But you had no plan in place and you "
                    "are not sure what to do.", 1)
        print_pause(f"The {bad_men} are huge and they have "
                    "lots of sophisticated weapons.", 1)
        print_pause("You have no weapon and the "
                    "men are strong and heavily armed.", 1)
        print_pause("You've lost!", 1)
    print_pause("Would you like to play again?")
    start_again()


def flee(weapons_holder):
    print_pause("You turn back and flee like your "
                "life depends on it because it sure does.", 1)
    print_pause("You are back to where the road "
                "divides into 2", 1)
    print_pause(f"Luckily, it seems the {bad_men} "
                "have choosen not to come after you.", 1)
    road_choice(weapons_holder)


def right_road():
    print_pause("You enter the road to your right.", 1)
    print_pause("You have barely taken two steps when "
                f"the {bad_men} come after you.", 1)
    print_pause("Would you like to fight or run away?", 1)


def left_road(weapons_holder):
    print_pause("You walk into the bright but narrow "
                "road to your left.", 1)
    if weapons in weapons_holder:
        print_pause("The road is a dead end. You have "
                    "picked all that was there.", 1)
        print_pause("You run back to the road", 1)
    else:
        print_pause("Soon enough, you discover that what "
                    "is making the road bright is a shiny "
                    f"metal {weapons}", 1)
        print_pause(f"You pick up the {weapons} and "
                    "run back to the junction.", 1)
        weapons_holder.append(weapons)
    road_choice(weapons_holder)


def start_again():
    play_again = valid_input("Enter y for yes and "
                             "n for no.\n", ["y", "n"])
    if play_again == "y":
        print_pause("Great choice! Restarting the "
                    "game...", 2)
        main_game()
    else:
        print_pause("Thanks for stopping by! Hope "
                    "to see you again soon.")
        exit(0)


def road_choice(weapons_holder):
    choose_road = valid_input("Which road will you like "
                              "to go?\n"
                              "Please enter 1 or 2\n", ["1", "2"])
    if choose_road == "1":
        right_road()
        fight_or_run = valid_input("Enter 1 to fight and 2 "
                                   "to run away.\n", ["1", "2"])
        if fight_or_run == "1":
            fight(weapons_holder)
        else:
            flee(weapons_holder)
    else:
        left_road(weapons_holder)


def main_game():
    global weapons
    global bad_men
    weapons = random.choice(weapons_list)
    bad_men = random.choice(bad_men_list)
    weapons_holder = []
    intro()
    road_choice(weapons_holder)


main_game()
