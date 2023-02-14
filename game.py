print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠟⠋⠙⠛⠉⠙⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣤⡤⢄⣀⣠⡏⠁⠀⠀⠀⠀⠀⠀⠀⠀⢳⣀⣠⣤⣤⣄⠀⠀⠀
⠀⠀⠀⣸⣿⣦⡀⠀⠉⠙⠲⠤⠤⠤⠤⠤⠤⠴⠚⠉⠁⠀⣠⣾⣿⡀⠀⠀
⠀⣀⣀⣿⣿⣿⣿⡶⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⣾⣿⣿⣿⣇⣀⠀
⣾⠋⠙⣻⣿⣿⡟⠀⠀⠈⣭⣟⠒⠒⠒⠒⢲⣯⡉⠀⠀⠈⢿⣿⡟⠁⠙⣧
⣿⠀⠀⠘⢿⡟⠀⠀⠀⠸⣿⣿⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠘⡿⠃⠀⠀⢻
⢻⣆⠀⠀⠀⠀⠀⠀⠀⡀⠉⠁⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾
⠀⠹⣤⡀⠀⠀⠀⠀⠀⢿⣶⣤⣤⣤⣤⣤⣤⣶⡾⠀⠀⠀⠀⠀⢀⣠⠞⠀
⠀⠀⠈⠛⣶⠀⠀⠀⠀⠀⠙⠿⢟⣉⣉⣻⠿⠋⠀⠀⠀⠀⢠⣶⠟⠁⠀⠀
⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡏⠀⠀⠀⠀
⠀⠀⠀⠀⠸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠷⢦⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⢳⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢶⣠⣤⣤⣤⣤⣤⣤⣤⣤⣴⠾⠛⠁⠀⠀⠀''')

print("*thud! You woke up. \n")
print("You found yourself in an abandoned asylum. \n")
print("The goal of the game is simply to navigate your way through the asylum and avoid ghost and monsters. \n")
print("You started walking. You look ahead and see 2 doors. The blue and red door. \n")

choice = input("You are to choose between 'blue' or 'red' door. Choose wisely: ")

if choice.lower() == "red":
    print("You entered the room full of banshee, They mauled you and it is GAME OVER!\n")
else:
    print("You proceeded safely tower upper lever.\n")
    
    choice = input("As you continue walking down the hall, you stumbled upon an weird looking glass. Will you take a look at it dare devil? Y or N: ")
    
    if choice.lower() == "y":
        print("You looked at the mirror and you see the underworld, you got sucked into it and it is now game over!.")
    else:
        print("Wise choice! You proceeded to the third floor safely! \n")
        
        choice = input("Mate! You've got some predicament here. So, infront of you is the door one leads to death, the other one gets you safely outside using the emergency exit. Which door will you take? Left or Right?: ")
        
        if choice.lower() == "right":
            print("Game over! You choosed the wrong door!\n")
        else:
            print("You got out safely out of the asylum.\n")