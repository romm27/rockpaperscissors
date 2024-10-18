# RUN main.py NOT THIS FILE! THIS IS ONLY A HEADER!
# Only use this class to define functions!

import datetime
import random

# Converts Ints to Unicode graphics, wow!
def int_to_unicode(_int):
    # Converts the choice int to unicode
    if _int == 0:  # Rock
        return "✊"
    if _int == 1:  # Paper
        return "🤚"
    if _int == 2:  # Scissors
        return "✌"
    return "ERRO"

def int_to_text(_int):
    # Converts the choice int to text
    if _int == 0:  # Rock
        return "Pedra"  # GetASCIIRock() <-- I planned to use ASCII art for text mode but regular text works better.
    if _int == 1:  # Paper
        return "Papel"  # GetASCIIPaper()
    if _int == 2:  # Scissors
        return "Tesoura"  # GetASCIIScissors()
    return "ERRO"

victory_matrix = [[0,2,2], [1,0,2], [1,1,0]]
#New and Improved Get Winner Check!
def get_winner(_player1, _player2): #0 - Draw, 1 - choice 1 wins, 2 - choice 2 wins.
    return victory_matrix[_player1][ _player2]

def print_outcome(_outcome, _mode):
    # Displays the state of the game at the end of a match
    player1 = "Jogador 1"
    player2 = "Jogador 2"

    # Convert name display to fit gamemode
    if _mode == 1:
        player1 = "Jogador"
        player2 = "CPU"
    if _mode == 2:
        player1 = "CPU 1"
        player2 = "CPU 2"

    if _outcome == 0:
        print("Empate!")
    elif _outcome == 1:
        print(player1, "vence!")
    elif _outcome == 2:
        print(player2, "vence!")

def process_input(_input):
    # Converts input to int
    temp = -1  # -1 means the input is invalid!

    try:
        temp = int(_input)  # If input is given as int
        if temp not in range(0, 3):  # Check for an invalid choice
            temp = -1  # Turn the result into an error
    except:
        tempText = _input.lower()  # If input is given as a string; also send it to lower case for ease of checking
        if tempText == "pedra" or tempText == "rock" or tempText == "r":
            temp = 0
        elif tempText == "papel" or tempText == "paper" or tempText == "p":
            temp = 1
        elif tempText == "tesoura" or tempText == "scissors" or tempText == "s" or tempText == "t":
            temp = 2

    if temp == -1:  # In case of no valid string given!
        print("Nenhum valor válido foi dado, o computador escolherá em seu lugar!")
        temp = make_ai_choice()

    return temp

def process_input_for_loop(_input):
    # Converts input to int
    temp = 0  # In the case of an invalid input, the game MUST GO ON!

    try:
        temp = int(_input)  # If input is given as int
    except:
        tempText = _input.lower()  # If input is given as a string; also send it to lower case for ease of checking
        if tempText == "continuar" or tempText == "c":
            temp = 0
        elif tempText == "sair" or tempText == "s":
            temp = 1

    return temp

def make_ai_choice():
    # Gets the bot's decision
    random.seed = datetime.datetime.now()  # Change seed to decrease the chance of draws in CPU vs CPU
    return random.randrange(3)

def print_battle_options():
    # Displays all available options
    print("#######Faça sua escolha######")
    print("0 - Pedra/Rock/R")
    print("1 - Papel/Paper/P")
    print("2 - Tesoura/Scissors/T/S")

def clear_view():
    # Clears the console view
    print('\n' * 100)

def print_final_results(_mode, _victories1, _victories2):
    # Prints the final result after the user wants to quit
    player1 = "Jogador 1"
    player2 = "Jogador 2"

    # Convert name display to fit gamemode
    if _mode == 1:
        player1 = "Jogador"
        player2 = "CPU"
    if _mode == 2:
        player1 = "CPU 1"
        player2 = "CPU 2"

    # Print Victory Table
    print('#' * 50)
    print(player1, "Vitórias totais:", _victories1)
    print(player2, "Vitórias totais:", _victories2)
    print("\n", end="")

    # Decide and print the final Winner
    print("Resultado final: ", end="")
    if _victories1 == _victories2:
        print(" Empate!")
    elif _victories1 > _victories2:
        print(player1, "Vence!")
    else:
        print(player2, "Vence!")

    print("Obrigado por jogar!")
    print("Desenvolvido por Giovanni Galarda Strasser. ☕")
    print('#' * 50)

# Graphical Prints for ASCII art
def print_logo():
    # Main Menu
    print(
        "| ) | \n|-' ,-. ,-| ;-. ,-: \n|"
        "   |-' | | | | | \n' `-' `-' ' `-` \n"
        "\n;-. . \n| ) | \n|-' ,-: ;-. ,-. | \n"
        "| | | | | |-' | \n' `-` |-' `-' ' `-` o ")
