name = input("Enter your name: ")
print("Welcome", name, "to this adventure!")
answer = input(
    "You are on a disastrous road, it has come to an end and you can go LEFT or RIGHT. Which way would you like to go? ").upper()

if answer == "LEFT":
    answer = input(
        "You come to a river, you can walk around it or swim accross? Type WALK to walk around and SWIM to swim accross: ").upper()

    if answer == "SWIM":
        print("You swam acrross and you won.")
    elif answer == "WALK":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print('Not a valid option. You lose.')

elif answer == "RIGHT":
    answer = input(
        "You come to a bridge, it looks wobbly, do you want to cross it or head back (CROSS IT/HEAD BACK)? ").upper()

    if answer == "HEAD BACK":
        print("You go back and lose.")
    elif answer == "CROSS IT":
        answer = input(
            "You cross the bridge and meet a stranger. Do you talk to them (YES/NO)? ").upper()

        if answer == "YES":
            print("You talk to the stanger and they give you gold. You WIN!")
        elif answer == "NO":
            print("You ignore the stranger and they are offended and you lose.")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

else:
    print('Not a valid option. You lose.')

print("Thank you for trying", name)