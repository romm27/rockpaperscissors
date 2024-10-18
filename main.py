import utilities

# Print Menu
utilities.print_logo()
print('\n' * 2)

# Build the prompt for choosing unicode characters.
unicodeExample = utilities.int_to_unicode(0) + utilities.int_to_unicode(1) + utilities.int_to_unicode(2)
unicodeExample = "1 - Unicode(" + unicodeExample + ")"

# Prompt user to input game settings
gamemode = int(input("Entre o modo de jogo\n0 - Player Contra Player\n1 - Player Contra IA\n2 - IA vs IA\n"))

graphics = int(input("Entre o modo gráfico\n0 - Texto(0 - Pedra, 1 - Tesoura, 2 - Papel)\n" + unicodeExample + "\n"))

# Clamp gamemode
gamemode = max(0, min(gamemode, 2))

# Clamp graphics
graphics = max(0, min(graphics, 1))

# Feedback the user graphic mode selection
if graphics == 0:
    print("\nExecutando em modo Texto! :)")
elif graphics == 1:
    print("\nExecutando em modo Unicode! 👍")
print('\n')

# Initialize global choice variables
choice1 = 0  # Player 1 choice
choice2 = 0  # Player 2 choice

# Score for each player
victories1 = 0
victories2 = 0
execute = True

# Main game loop!
while execute:
    # Handle Game Loop for each gamemode!
    if gamemode == 0:  # PVP
        utilities.print_battle_options()
        choice1 = utilities.process_input(input("Primeiro Jogador:"))
        utilities.clear_view()  # Hide first player's choice
        utilities.print_battle_options()
        choice2 = utilities.process_input(input("Segundo Jogador:"))
    elif gamemode == 1:  # PVE
        utilities.print_battle_options()
        choice1 = utilities.process_input(input("Escolha do Jogador:"))
        choice2 = utilities.make_ai_choice()
        botChoiceDisplay = ""
        if graphics == 0:
            botChoice = utilities.int_to_text(choice1)
        elif graphics == 1:
            botChoice = utilities.int_to_unicode(choice2)
        print("Escolha da IA:", botChoiceDisplay)  # Print Bot Choice
    elif gamemode == 2:  # CPU vs CPU
        utilities.print_battle_options()
        choice1 = utilities.make_ai_choice()
        choice2 = utilities.make_ai_choice()
        botChoiceDisplay = ""
        if graphics == 0:
            botChoice = utilities.int_to_text(choice2)
        elif graphics == 1:
            botChoice = utilities.int_to_unicode(choice2)
        print("Escolha da IA:", botChoiceDisplay)  # Print Bot Choice
        utilities.clear_view()

    # Process Match results
    player1Print = ""
    player2Print = ""
    vsPrint = ""

    # Process Graphics Choice
    if graphics == 0:
        player1Print = utilities.int_to_text(choice1)
        player2Print = utilities.int_to_text(choice2)
        vsPrint = "vs"
    elif graphics == 1:
        player1Print = utilities.int_to_unicode(choice1)
        player2Print = utilities.int_to_unicode(choice2)
        vsPrint = "vs"

    # Print Result
    print(player1Print, vsPrint, player2Print)
    winner = utilities.get_winner(choice1, choice2)
    utilities.print_outcome(winner, gamemode)

    # Set player names based on gamemode
    player1Name = "Jogador 1"
    player2Name = "Jogador 2"

    if gamemode == 1:
        player1Name = "Jogador"
        player2Name = "CPU"
    if gamemode == 2:
        player1Name = "CPU 1"
        player2Name = "CPU 2"

    # Print Final Score
    if winner == 0:
        print(player1Name, ">", victories1, "Vitórias (-)")
        print(player2Name, ">", victories2, "Vitórias (-)")
    elif winner == 1:
        victories1 += 1
        print(player1Name, ">", victories1, "Vitórias (+1)")
        print(player2Name, ">", victories2, "Vitórias")
    elif winner == 2:
        victories2 += 1
        print(player1Name, ">", victories1, "Vitórias")
        print(player2Name, ">", victories2, "Vitórias (+1)")

    # End of loop / Check if User wishes to continue
    print('\n' * 2)
    prompt = utilities.process_input_for_loop(input("Gostaria de Continuar ou Sair?\n0 - Continuar/C\n1 - Sair/S\n"))
    execute = prompt == 0  # Continue game with any other prompt other than 1 or 'continuar'

if not execute:
    utilities.print_final_results(gamemode, victories1, victories2)  # Print final results and credits.
else:
    utilities.clear_view()
