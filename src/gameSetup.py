'''Here is the file where we are going to doing our setting
up, such as the width, height etc
'''

class setup:
    '''
    several things we will need here might include:
    1.) Size of block
    2.) width and height of map
    3.) If we want to make the game advanced, then we can have a
    camera follow our player and then in that case we might
    need a render_width and render_height for the width and 
    height that will be rendered based on the view point
    4.) width and height of screen
    '''
    blockSize = 64 #8*8
    screenWidth = 600
    screenHeight=500
    mapWidth = 100
    mapHeight = 200
    renderWidth = 50
    renderHeight = 100

    def __init__(self) -> None:
        pass

        