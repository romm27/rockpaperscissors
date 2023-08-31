#Use this class to define functions!

#Converts Ints to Unicode graphics, wow!
def IntToUnicode(_int):
    if _int == 0:  # Rock
        return "✊"
    if _int == 1:  # Scissors:
        return "✌"
    if _int == 2:  # Paper:
        return "🤚"
    return "ERRO"

#Replaces the given section of the console with a hidden version of the choices from each player...
def HideChoice(_text):
    temp = str.replace(_text, "✊", "*")
    temp = str.replace(_text, "✌", "*")
    temp = str.replace(_text, "🤚", "*")
    return temp

#Returns the winner of a battle.
def GetWinner(_choice1, _choice2): #0 - Draw, 1 - choice 1 wins, 2 - choice 2 wins.
    #Edge Cases
    if _choice1 == _choice2: return 0 #Draw
    if _choice1 == 2 and _choice2 == 0: return 1 # paper vs rock
    if _choice2 == 2 and _choice1 == 0: return 2 # paper vs rock

    #Most Cases
    if _choice1 < _choice2: return 1
    if _choice1 > _choice2: return 2

def OutComeToText(_outcome):
    if _outcome == 0:
        return "Empate!"
    elif _outcome == 1:
        return


#def PrintBattle(_choice1, _choice2):
