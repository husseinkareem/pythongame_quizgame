import classdrivers
from time import sleep



class MainMenu:                                                                                            
    
    def __init__(self, isPlaying = False):
        self.isPlaying = isPlaying
        
        print(
            "\nCOUNTDOWN TO IMPLOSION\nYet another awardwinning masterpiece from Aldo, Husse and Jacke.\n\n"
            "For some reason, the Universe will implode if humanity doesn't embark on a voyage out into the\n"
            "vast voids in search for five relics. It's up to you, dear player, and you must find them all\n"
            "and break their seals by answering three very relevant existensial questions before it's too late\n"
            "Hurry! The implosion will accur in only 20 turns!\n\n"                             
            "[1] Start Game\n[2] Quit\n",
        )  

    def setStartGame(self):   
        self.isPlaying = classdrivers.inputStartGame()                                                                          
        return self.isPlaying 

    def setNewGame(self):
        print("\nDo you want to save the Universe again?\n\n[1] Of course!\n[2] Hell no.\n")
        self.isPlaying = classdrivers.inputStartGame()                                                                          
        return self.isPlaying                                                                                #END

class ShipConfiguration: 
    '''ShipConfiguration class.'''
    def __init__(self, shipName, shipType, shipTravelTurnCost, shipCatchTurnCost):
        self.shipName = shipName
        self.shipType = shipType
        self.shipTravelTurnCost = shipTravelTurnCost
        self.shipCatchTurnCost = shipCatchTurnCost

    def setShipName(self):
        '''sets shipName by userinput'''
        self.shipName = classdrivers.inputShipName()                                                                            #   -> classrivers
        print("\nReally? You're called for saving the universe and name your ship {} ?\nNevermind...".format(self.shipName))
        sleep(1)

    def setShipType(self):
        '''sets shipType by userinput'''
        self.shipType = classdrivers.inputShipType()                                                                            #   -> classrivers
        print("\nNice! You've picked the {}.".format(self.shipType))

#       to better understand the deal with upcoming "shipTravelTurnCost" and "shipCatchTurnCost",
#       see doc-string in the setTurnRemaining-method within the ShipNavigator class.
    
    def setShipTravelTurnCost(self):
        '''sets the shipTravelTurnCost-attribute'''
        #self.shipTravelTurnCost = 2 if self.shipType == "Carrier" else 1
        if self.shipType == "Carrier":
            self.shipTravelTurnCost = 2
        else:
            self.shipTravelTurnCost = 1

    def setShipCatchTurnCost(self):
        '''sets the shipCatchTurnCost-attribute'''
        #self.shipCatchTurnCost = 1 if self.shipType == "Carrier" else 2
        if self.shipType == "Carrier":
            self.shipCatchTurnCost = 1
        else:
            self.shipCatchTurnCost = 2

    def getShipName(self):
        '''returns shipName.'''
        return self.shipName

    def getShipType(self):
        '''returns shipType.'''
        return self.shipType

    def getShipTravelTurnCost(self):
        '''returns shipTravelTurnCost.'''
        return self.shipTravelTurnCost

    def getShipCatchTurnCost(self):
        '''returns shipCatchTurnCost.'''
        return self.shipCatchTurnCost

class ShipNavigator:
    '''
    ShipNavigator class. inherits an instance of the ShipConfiguration class.
    
    think of this class as a module on the Bridge keeping track of/snapping up all relevant data about what's going on in an abstract space.
    this data is being calculated and used for driving the game forward and for creating "UI" in this very graphic intense game.
    '''
    def __init__(self, shipConfiguration: ShipConfiguration, previousCommand, currentCommand, nextTile, planetsVisited, turnsRemaining, destinationCount):
        self._shipConfiguration = shipConfiguration
        self.previousCommand = previousCommand
        self.currentCommand = currentCommand
        self.nextTile = nextTile
        self.planetsVisited = planetsVisited
        self.turnsRemaining = turnsRemaining
        self.destinationCount = destinationCount

    def setPreviousCommand(self):
        '''sets previousCommand with the value of currentCommand before the latter recieves a new value.'''
        self.previousCommand = self.currentCommand

    def setCurrentCommand(self):
        '''sets currentCommand'''
        self.currentCommand = classdrivers.commandEngine(self.previousCommand)                                                  #   -> classrivers

    def setNextTile(self):
        '''sets nextTile before running a little "travel-animation".'''
        self.nextTile = classdrivers.generateTiles(self.currentCommand)                                                         #   -> classrivers
        
        traveling = ["\nTraveling.", "Traveling..", "Traveling...", "\n{} Reached".format(self.currentCommand)]
        for travel in traveling:
            sleep(0.3)
            print(travel)
        
    def setPlanetsVisited(self):
        '''
        sets planetsVisited by adding 1 to itself when called (implicit used as an "iterator" in the OrbitScene()-function).
        '''
        self.planetsVisited += 1

    def setTurnsRemaining(self, tileFlag):
        '''
        shiptype "Carrier" consumes 2 turns while traveling and 1 turn for catching an artifact.
        shiptype "Vulture" consumes 1 turn while traveling but needs 2 turns for catching an artifact.

        this method going to take these values in account each time it's called for calculating turnsRemaining.
        '''
        travelTurnCost = self._shipConfiguration.getShipTravelTurnCost()
        catchTurnCost = self._shipConfiguration.getShipCatchTurnCost()
        shipType = self._shipConfiguration.getShipType()
        
        sleep(1)

        if tileFlag == 'void':
            self.turnsRemaining -= travelTurnCost
            print("\n[You encountered just another void part of the Universe. You suck]\n")
            print("[Your {} consumed {} turn(s) while travelling]".format(shipType, travelTurnCost))

        elif tileFlag == "warp":
            self.turnsRemaining += 1    #   same for both shiptypes.
            print("\n[You encountered a warpzone! You'll gain turns because... physics]\n")
            print("[Your {} gained {} turn(s) in the timewarp]".format(shipType, travelTurnCost))
        else:
            self.turnsRemaining -= catchTurnCost
            self.turnsRemaining -= travelTurnCost
            print("\n[Your {} consumed {} turn(s) while catching the artifact]".format(shipType, catchTurnCost))
            print("[Your {} consumed {} turn(s) while travelling]".format(shipType, travelTurnCost))

        sleep(1)

        print("[{} turns left until implosion]\n".format(self.turnsRemaining))

        sleep(1)

    def getPreviousCommand(self):
        '''returns previousCommand.'''
        return self.previousCommand

    def getCurrentCommand(self):
        '''returns currentCommand.'''
        return self.currentCommand

    def getPlanetsVisited(self):
        '''returns the current count of planets visited.'''
        return self.planetsVisited

    def getNextTile(self):
        '''returns nextTile.'''
        return self.nextTile

    def getTurnsRemaining(self):
        '''returns turnsRemaining.'''
        return self.turnsRemaining

class Artifact:
    '''Artifact class'''
    def __init__(self, artifactName, quizBlockNumber):
        '''the deal with quizBlockNumber-attribute is clarified in the artifactQuestions-function.'''
        self.artifactName = artifactName
        self.quizBlockNumber = quizBlockNumber

    def getArtifactName(self):
        '''
        runs imported logic from the artifactQuestion-function whereas user answers a given set of questions to "break the seal".
        returns the artifact when the questions have been dealt with in the form of its name (string).
        '''
        sleep(1)
        print("\nTo obtain the artifact, answer upcoming three questions!")
        sleep(1)
        classdrivers.artifactQuestions(self.quizBlockNumber)                                                                #   -> classrivers
        sleep(1)
        print("\nArtifact {} recieved!".format(self.artifactName))
        sleep(1)
        return self.artifactName

class Planet:
    '''Planet class, inherits an instance from the Artifact class.'''
    def __init__(self, artifact: Artifact, planetName):
        self._artifact = artifact
        self.planetName = planetName

    def getPlanetName(self):
        '''returns name of the planet.'''
        return self.planetName

class SpaceShip():
    '''
    SpaceShip class. inherits an instance of the ShipNavigator class.
    '''
    def __init__(self, shipNavigator: ShipNavigator):
        self._shipNavigator = shipNavigator
        self.storedArtifacts = []
        self.currentPlanet = None
        self.currentArtifact = None

    def launch(self):
        '''a little animation for launching the ship.'''
        sleep(1)
        print("\nNow, Let's light this candle up :D !")
        sleep(1)
        launchCountDown = ["\n3", "\n2", "\n1", "\nBOOM!!!\n"]
        for count in launchCountDown:
            print(count)
            sleep(1)

    def setCurrentPlanet(self, planetList: list[Planet]):
        '''
        ulilizing the value stored in the "navigator-module's" planetVisited-attribute making sure the game loads the
        correct planet-object from the planetList.
        '''
        currentPlanetIndex = self._shipNavigator.getPlanetsVisited()
        self.currentPlanet = planetList[currentPlanetIndex]
        sleep(1)
        print("You've discovered planet {}!".format(self.currentPlanet.planetName))

    def setCurrentArtifact(self, planetList: list[Planet]):
        '''
        ulilizing the value stored in the "navigator-module's" planetVisited-attribute making sure the game loads the
        correct artifact-object from the planetList (every planet has an inherited Artifact object).
        '''
        currentPlanetIndex = self._shipNavigator.getPlanetsVisited()
        self.currentArtifact = planetList[currentPlanetIndex]._artifact
        sleep(1)

        print("You've detected artifact {}!".format(self.currentArtifact.artifactName))

    def getCurrentPlanet(self):
        '''returns the planet we're dealing with at the moment/just descovered.'''
        return self.currentPlanet

    def getCurrentArtifact(self):
        '''returns the artifact that dwells on the planet we're dealing with at the moment/just descovered.'''
        return self.currentArtifact

    def catchArtifact(self):
        '''calls the getArtifact-method on the current artifact.'''
        self.currentArtifact.getArtifactName()

    def storeArtifact(self):
        '''stores (appends) the name of the current artifact.'''
        self.storedArtifacts.append(self.currentArtifact.artifactName)
    
    def viewArtifacts(self):
        '''enumerates and prints the current list of the (hopefully) ever growing collection of artifacts catched.'''
        currentCatch = 0
        maxCatch = 5
        
        print("\nCurrent artifacts collected\n----------------------------\n")
        
        for artifact in enumerate(self.storedArtifacts):
            currentCatch += 1
            print("{}   {}".format(artifact[0] + 1, artifact[1]))
        print("\n----------------------------\n")
        
        catchToGo = maxCatch - currentCatch
        print("({} artifacts left to catch)".format(catchToGo))

    def ensambleArtifacts(self):
        '''goofy way of simulate the very ensamble.'''
        art = self.storedArtifacts 
        sleep(1)
        print(
            "\nVICTORY!\nYOU'VE CATCHED ALL ARTIFACTS BEFORE THE TIME RAN OUT.\n\n"
            "The only thing left to do is to ensamble them all into something that's going\n"
            "to defeat whatever it is threatening the Universe.\n"
        )
        sleep(2)
        print("*ENSAMBLING*\n")
        sleep(2)
        print(
            "By cracking the {} and fill it with a {} before marinade it all throughout the night with {} in a {}\n"
            "while recording it all on a {} you've created the movie 'Cable Guy' from 1996 with Jim Carrey int the lead!\n"
            .format(art[0], art[1], art[2], art[3], art[4])
        )
        sleep(5)
        print(
            "By holding this awful thing, this worst piece of crap ever made, in front of <whatever imploding the universe> you've successfully\n"
            "chased it away in pain and saved the day.\n\nWell done you."
        )