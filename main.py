def on_a_pressed():
    global Jump, Vy
    Jump = 1
    Vy = 1
    for index in range(7):
        Palyer.y += Vy * -1
        Vy += 1
        pause(100)
    Jump = 0
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_right_repeated():
    Palyer.x += 1
controller.right.on_event(ControllerButtonEvent.REPEATED, on_right_repeated)

def on_left_repeated():
    Palyer.x += -1
controller.left.on_event(ControllerButtonEvent.REPEATED, on_left_repeated)

Vy = 0
Jump = 0
Palyer: Sprite = None
Palyer = sprites.create(img("""
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
    """),
    SpriteKind.player)
scene.camera_follow_sprite(Palyer)
scene.set_background_color(9)
Palyer.y = 90
game.show_long_text("Hello", DialogLayout.BOTTOM)
tiles.set_current_tilemap(tilemap("""
    niveau3
"""))

def on_forever():
    if Jump == 0:
        Palyer.y += 2
        pause(100)
forever(on_forever)
