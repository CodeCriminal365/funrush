namespace SpriteKind {
    export const GUI = SpriteKind.create()
    export const floor = SpriteKind.create()
}
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    moveUp(permPixels)
})
function moveRight (pixels: number) {
    mainPlayer.setVelocity(pixels, pixels / 5)
}
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    mainPlayer.setVelocity(0, 0)
})
function moveUp (pixels2: number) {
    mainPlayer.setVelocity(pixels2 / 5, pixels2)
}
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    moveLeft(permPixels)
})
function moveDown (pixels3: number) {
    mainPlayer.setVelocity(pixels3 - pixels3 * 2, pixels3 / 5)
}
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    moveRight(permPixels)
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    moveDown(permPixels)
})
function moveLeft (pixels4: number) {
    mainPlayer.setVelocity(pixels4 - pixels4 * 2, pixels4 / 5)
}
let permPixels = 0
let mainPlayer: Sprite = null
mainPlayer = sprites.create(assets.image`character`, SpriteKind.Player)
mainPlayer.setPosition(63, 74)
scene.setBackgroundImage(assets.image`skyBox`)
forever(function () {
    permPixels = 25
    mainPlayer.setStayInScreen(true)
    mainPlayer.setBounceOnWall(true)
})
