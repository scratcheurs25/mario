controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    Jump = 1
    Vy = 1
    for (let index = 0; index < 7; index++) {
        Palyer.y += Vy * -1
        Vy += 1
        pause(100)
    }
    Jump = 0
})
controller.right.onEvent(ControllerButtonEvent.Repeated, function () {
    Palyer.x += 1
})
controller.left.onEvent(ControllerButtonEvent.Repeated, function () {
    Palyer.x += -1
})
let Vy = 0
let Jump = 0
let Palyer: Sprite = null
Palyer = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . f f f f f f f . . . . . 
    . . . f 4 4 4 4 5 5 5 f . . . . 
    . . . f 4 4 4 4 4 4 5 f . . . . 
    . . . f 4 4 4 4 4 4 5 f . . . . 
    . . . f 4 4 4 4 4 4 4 f . . . . 
    . . . f 4 4 4 4 4 4 4 f . . . . 
    . . . f 4 4 4 4 4 4 4 f . . . . 
    . . . f 4 4 4 4 4 4 4 f . . . . 
    . . . f 4 4 4 4 4 4 4 f . . . . 
    . . . . f f f f f f f . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.Player)
scene.cameraFollowSprite(Palyer)
scene.setBackgroundColor(9)
Palyer.y = 90
game.showLongText("Hello", DialogLayout.Bottom)
tiles.setCurrentTilemap(tilemap`niveau3`)
forever(function () {
    if (Jump == 0) {
        Palyer.y += 2
        pause(100)
    }
})
