@namespace
class SpriteKind:
    GUI = SpriteKind.create()
    floor = SpriteKind.create()
def moveRight(pixels: number):
    mainPlayer.set_velocity(pixels, pixels / 5)
def moveUp(pixels2: number):
    mainPlayer.set_velocity(pixels2 / 5, pixels2)

def on_a_pressed():
    moveUp(25)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    moveLeft(25)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def moveDown(pixels3: number):
    mainPlayer.set_velocity(pixels3 - pixels3 * 2, pixels3 / 5)

def on_right_pressed():
    moveRight(25)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def moveLeft(pixels4: number):
    mainPlayer.set_velocity(pixels4 - pixels4 * 2, pixels4 / 5)
mainPlayer: Sprite = None
mainPlayer = sprites.create(assets.image("""
    character
"""), SpriteKind.player)
mainPlayer.set_position(63, 74)
scene.set_background_image(assets.image("""
    skyBox
"""))

def on_forever():
    if mainPlayer.y <= 112:
        mainPlayer.vy += 5
    else:
        if mainPlayer.y >= 112:
            moveDown(25)
forever(on_forever)
