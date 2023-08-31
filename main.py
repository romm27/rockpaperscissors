#The main game steps are processed here, ((NEVER)) redirect the flow to another file.
import utilities

graphics = 0 #0 - binary, 1 - unicode, 2 - console art

#Menu
print("Pedra Papel Tesoura!")

#Build the prompt for Unicode character.
#It is done this way so that in the case of a character change it is automatically updated.
unicodeExample = utilities.IntToUnicode((0))
unicodeExample = unicodeExample.__add__(utilities.IntToUnicode((1)))
unicodeExample = unicodeExample.__add__(utilities.IntToUnicode((2)))
unicodeExample = "1 - Unicode(".__add__(unicodeExample).__add__(")")

#0 - PvP, 1 - PvE- 2 - EvE
gamemode = int(input("Entre o modo de jogo \n0 - Player Contra Player \n1 - Player Contra IA \n2 - IA vs IA\n"))
graphics = int(input("Entre o modo gráfico \n0 - Texto(0,1,2) \n".__add__(unicodeExample).__add__("\n2 - Gráficos 2D\n")))

choice1 = int(input("1:"))
choice2 = int(input("2:"))
print(utilities.IntToUnicode(choice1), " vs ", utilities.IntToUnicode(choice2))
print(utilities.GetWinner(choice1, choice2))