namespace SpriteKind {
    export const GUI = SpriteKind.create()
    export const floor = SpriteKind.create()
}
function moveRight (pixels: number) {
    mainPlayer.setVelocity(pixels, pixels / 5)
}
function moveUp (pixels2: number) {
    mainPlayer.setVelocity(pixels2 / 5, pixels2)
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    moveUp(25)
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    moveLeft(25)
})
function moveDown (pixels3: number) {
    mainPlayer.setVelocity(0, pixels3 / 5)
}
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    moveRight(25)
})
function moveLeft (pixels4: number) {
    mainPlayer.setVelocity(pixels4 - pixels4 * 2, pixels4 / 5)
}
let mainPlayer: Sprite = null
mainPlayer = sprites.create(assets.image`character`, SpriteKind.Player)
mainPlayer.setPosition(63, 74)
scene.setBackgroundImage(assets.image`skyBox`)
forever(function () {
    if (mainPlayer.y >= 100) {
        mainPlayer.vy += 5
    } else {
        if (mainPlayer.y <= 100) {
            moveDown(25)
        }
    }
})
