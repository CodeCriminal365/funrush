@namespace
class SpriteKind:
    GUI = SpriteKind.create()
    floor = SpriteKind.create()

def on_up_pressed():
    moveUp(permPixels)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def moveRight(pixels: number):
    mainPlayer.set_velocity(pixels, pixels / 5)

def on_b_pressed():
    mainPlayer.set_velocity(0, 0)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def moveUp(pixels2: number):
    mainPlayer.set_velocity(pixels2 / 5, pixels2)

def on_left_pressed():
    moveLeft(permPixels)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def moveDown(pixels3: number):
    mainPlayer.set_velocity(pixels3 - pixels3 * 2, pixels3 / 5)

def on_right_pressed():
    moveRight(permPixels)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_down_pressed():
    moveDown(permPixels)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def moveLeft(pixels4: number):
    mainPlayer.set_velocity(pixels4 - pixels4 * 2, pixels4 / 5)
permPixels = 0
mainPlayer: Sprite = None
mainPlayer = sprites.create(assets.image("""
    character
"""), SpriteKind.player)
mainPlayer.set_position(63, 74)
scene.set_background_image(assets.image("""
    skyBox
"""))

def on_forever():
    global permPixels
    permPixels = 25
    mainPlayer.set_stay_in_screen(True)
    mainPlayer.set_bounce_on_wall(True)
forever(on_forever)
