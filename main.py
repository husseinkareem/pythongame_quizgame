from classes import MainMenu, ShipConfiguration, ShipNavigator, Artifact, Planet, SpaceShip


def artifactListSetup():
    '''creates 5 artifact-objects from the Artifact-class before returning them in a list.'''
    artifactOne = Artifact("Coconut", 0)
    artifactTwo = Artifact("Roadkill", 1)
    artifactThree = Artifact("Swedish 'Fiskbullar'", 2)                          
    artifactFour = Artifact("Mulch", 3)
    artifactFive = Artifact("Nokia NGage", 4)

    artifactList = [artifactOne, artifactTwo, artifactThree, artifactFour, artifactFive]

    return artifactList

def planetListSetup(artifactList: list[Artifact]):
    '''creates 5 planet-objects, partly by inherit artifact-objects (list in input) and distribute them among the planets.'''
    planetOne = Planet(artifactList[0], "Jupiter")                                                            
    planetTwo = Planet(artifactList[1], "Mars")
    planetThree = Planet(artifactList[2], "Neptunus")                             
    planetFour = Planet(artifactList[3], "Saturnus") 
    planetFive = Planet(artifactList[4], "Venus")                              

    planetList = [planetOne, planetTwo, planetThree, planetFour, planetFive] 

    return planetList

def spaceshipSetup():
    '''
    a shipConfiguration-object being created. by calling the two methods dealing with namegiving and "shiptyping" on the new object,
    the last two methods sets properties based on the choosen shipType.

    next we create an object from the ShipNavigator-class, inherits the configuration, and let it be part of the very ship. return.
    '''
    startTurns = 20
#   turns remaining (start of the game)

    shipConfiguration = ShipConfiguration("default", "default", 0, 0)

    shipConfiguration.setShipName()
    shipConfiguration.setShipType()
    shipConfiguration.setShipTravelTurnCost()
    shipConfiguration.setShipCatchTurnCost()

    shipNavigator = ShipNavigator(
        shipConfiguration, "start", "start", "yetUnknown", 0, startTurns, 0
    )

    spaceship = SpaceShip(shipNavigator)

    return spaceship

#   the upcoming "-Scenefunctions" is an attempt of making abstract sense of various methodcalls throughout the game.
#   look at it as something like:

#       1) universeScene()      - here we travel by...
#       2) commandingScene()    - calling the commandingScene and if we encounter a planet...
#       3) orbitScene()         - we enter the orbitScene and start catching artifacts.

def universeScene():
    '''
    the "core-function" of the very gameplay.
    
    here we call the functions that create the artifacts, planets and the spaceschip before we "launch" the latter out in "the Universe".
    the while-loop won't break before 'turnsRemaining' reaches 0 or below (player lost the game) or 5 planets being visited (player won the game).
    ...or the program bites the dust/[CTRL+C].
    '''
    artifactList = artifactListSetup()
    planetList = planetListSetup(artifactList)
    spaceship = spaceshipSetup()

    spaceship.launch()

    while spaceship._shipNavigator.getTurnsRemaining() > 0:
        
        commandingScene(spaceship)
        
        if spaceship._shipNavigator.getNextTile() == "void":
            spaceship._shipNavigator.setTurnsRemaining("void")

        elif spaceship._shipNavigator.getNextTile() == "warp":
            spaceship._shipNavigator.setTurnsRemaining("warp")
            
        else:
            orbitScene(spaceship, planetList)
            spaceship._shipNavigator.setTurnsRemaining("planet")
            if spaceship._shipNavigator.getPlanetsVisited() == 5:
                spaceship.ensambleArtifacts()
                return
    print(
        "DISASTER!\n"
        "YOU DIDN'T MANAGE TO COLLECT ALL ARTIFACTS IN TIME AND THE UNIVERSE IMPLODED."
    )

def commandingScene(spaceship: SpaceShip):
    '''
    methods being called dealing with navigation from the spaceship (more specific from the inherited "shipnavigator").
    '''
    spaceship._shipNavigator.setPreviousCommand()
    spaceship._shipNavigator.setCurrentCommand()
    spaceship._shipNavigator.setNextTile() 

def orbitScene(spaceship: SpaceShip, planetList: list[Planet]):
    '''
    methods being called dealing with logic covering "artifact-gathering". except the spaceship-object we're using the planetList
    as an input while working on its elements.
    '''
    spaceship.setCurrentPlanet(planetList)
    spaceship.setCurrentArtifact(planetList)
    spaceship.catchArtifact()
    spaceship.storeArtifact()
    spaceship.viewArtifacts()

    spaceship._shipNavigator.setPlanetsVisited()
    
                                                                                 
def main():                                                                                 
   
    mainMenu = MainMenu()                                                  
    isPlaying = mainMenu.setStartGame()                            
      
    while isPlaying == True:
        universeScene()
        isPlaying = mainMenu.setNewGame()
                                          
if __name__ == '__main__':
        main()    