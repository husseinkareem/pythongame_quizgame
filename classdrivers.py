import random                                                                                           

def inputStartGame():                                                                   
    startGame = input("select> ")

    if startGame.isalpha() or startGame == "" or (int(startGame) < 1 or int(startGame) > 2):
        print("Two choices, start a new game (1) or Quit (2)\n")
        return inputStartGame()

    elif int(startGame) == 1:
        print("\nAllright! Before saving the Universe, you need to prepare your ship.")
        return True

    else:
        print("\nBye!\n")
        return False                                                                                     #

def inputShipName():                                                                    
    '''
    the program asks the player to enter a name on the spaceship. violation of desired inputformat
    and the func being run again recursively.
    '''
    print("\nChooce a dynamite name for your ride.\n-------------------------------------\n")
    shipName = input("Name on Spaceship> ")

    if len(shipName) < 1:
        print("On an important voyage like this, you should name your ship with at least one charachter!\n")
        return inputShipName()
    
    return shipName

def inputShipType():
    '''
    user picks a shipType, "Carrier" or "Vulture". violation of desired inputformat
    and the func being run again recursively.
    '''
    print(
        "\nSelect type of ship.\n----------------------\n"
        "[1] Carrier:\tIt's a big ship taking its time to move around (2 turns/travel) but it's produktive.\n"
        "\t\tWell in an orbit it just cost 1 turn to detect and catch an artifact.\n\n"
        "[2] Vulture:\tA fast ship (1 turn/travel) but it costs 2 turns to detect and catch an artifact.\n\n"
    )

    shipType = input("Chooce shipType> ")                                                                           

    if shipType.isalpha() or shipType == "" or (int(shipType) < 1 or int(shipType) > 2):
        print("You can only choose between a 'Carrier' and a 'Vulture' (1 or 2), try again.")
        return inputShipType()                                           
    
    if int(shipType) == 1:
        return "Carrier"

    return "Vulture"

def commandEngine(previousCommand): 
    '''
    a menu of possible directions/courses are served the player who choose by enter a corresponding integer 1 - 4. this integer is
    represented as a key in a dictionary as well and its pair-value ("North", "South" etc.) is what the function finally returns.
    if the user tries to "go back" (checked by previousCommand) or violates inputformats the func being run again recursively.
    '''
    print("Where do you want to go next?\n-----------------------------\n[1] North\n[2] West\n[3] East\n[4] South\n")
    
    command = input("navigate> ")

    if command.isalpha() or command == "" or (int(command) < 1 or int(command) > 4):
        print("You tried to enter anything but a digit between 1 and 4.\n")
        return commandEngine(previousCommand)                             
    
    command = int(command)
    navigationChoises = {1: "North", 2: "West", 3: "East", 4: "South"}
    
    if (
        (navigationChoises[command] == "South" and previousCommand == "North") or
        (navigationChoises[command] == "North" and previousCommand == "South") or
        (navigationChoises[command] == "West" and previousCommand == "East") or
        (navigationChoises[command] == "East" and previousCommand == "West")):
        
        print("\nYou just came from the {}! Try another course!\n".format(navigationChoises[command]))
        return commandEngine(previousCommand)

    currentCommand = navigationChoises[command] 
    return currentCommand

def generateTiles(currentCommand):
    '''
    utilizes the random-library, more specific the shuffle-method, for shuffling a hardcoded list of possible outcomes around.
    the currentCommand input ("North", "South" etc.) decides witch element ("tile" in the list) the ship going to visit next.
    '''
    nextTile = None
    randomTileList = ["void", "warp", "planet", "void"]
    random.shuffle(randomTileList)
    
    if currentCommand == "North":
        nextTile = randomTileList[0]
    
    elif currentCommand == "West":
        nextTile = randomTileList[1]
    
    elif currentCommand == "East":
        nextTile = randomTileList[2]
    else:
        nextTile = randomTileList[3]                                         

    return nextTile

#   upcoming 'artifactQuestions' and 'answerQuestions' are two functions working togheter, the latter within the former.
    
def artifactQuestions(quizBlockNumber):
    '''
    the game's 5 Artifact-objects are being assigned an unique integer (0-4) stored in the quizBlockNumber attribute.
    the qestionsets (lists of tuples) declared below (and collected in a list themselves) is one by one fed into the
    answerQuestions-function by its index (quizBlockNumber) throughout the game.
    '''

    quizBlockOne = [                                            
        ("\nCorrect syntax to output 'Hello World' in python?\n(a) print('Hello World'):  \n(b)input('Hello World'):  ", "a"),
        ("\nHow do you insert COMMENTS in Python code?\n(a) #:  \n(b) Comments: ", "a"),
        ("\nWhat is the correct file extension for Python files?\n(a) .python:  \n(b) .py: ", "b")
    ]
    quizBlockTwo = [
        ("\nWhich operator is used to multiply numbers?\n(a) x : \n(b) * : ", "b"),
        ("\nWhich operator can be used to compare two values?\n(a) = :  \n(b)== : ", "b"),
        ("\nWhich statement is used to stop a loop?\n (a) Break:  \n (b) Else: ", "a")
    ]
    quizBlockThree = [
        ("\nWhich collection is ordered, changeable, and allows duplicate members?\n (a) List:  \n(b) loop: ", "a"),
        ("\nWhat is the result of print(type({}) is set)\n(a) True:  \n(b) False: ", "b"),
        ("\nWhich is most popular programming languages?\n(a) Javascript:  \n(b) Python: ", "b")
    ]
    quizBlockFour = [
        ("\nTo return the length of string, What command do we use?\n(a) str():  \n(b) len(): ", "b"),
        ("\nIn order to store values in terms of key and value pair, what type of core datatype we need?\n(a) Dict:  \n(b) List: ", "a"),
        ("\nThe format() function returns?\n(a) str():  \n(b) int(): ", "a")
    ]
    quizBlockFive = [
        ("\nPython first year appeared in?\n(a) 1991:  \n(b) 1995: ", "a"),
        ("\nPython is designed by?\n(a) Guido van Rossum:  \n(b) Brendan Eich: ", "a"),
        ("\nWhat is the data type of print(type(10))\n(a) float:  \n(b) int:  ", "b")
    ]

    quizBlocks = [quizBlockOne, quizBlockTwo, quizBlockThree, quizBlockFour, quizBlockFive]
    answerQuestions(quizBlocks[quizBlockNumber])

def answerQuestions(currentQuizBlock):
    '''
    a given set of questions (list of tuples) is loaded into the function. the user answers the question in every tuple (q,)
    and the game checks if it's correct with its pair-value (,a). if not 3 out of 3 correct, the func being run again recursively.
    in other words, the player can't catch the artifact (and continue the game) until he or she answers correct on all 3 current questions.
    '''
    correct = 0

    for question in currentQuizBlock:
        answer = input(question[0])
        if answer == question[1]:
            correct += 1                                                    
    
    if correct != 3:
        print("\nYou've entered a wrong answer! To obtain artifact you need 3(3) correct.\n")
        return answerQuestions(currentQuizBlock)