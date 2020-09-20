from pico2d import *
from gobj import *

def enter():
    global grass, team
    grass = Grass()
    team = [ Boy() for i in range(11) ]

def update():
    for b in team: b.update()

def draw():
    grass.draw()
    for b in team: b.draw()

def handle_events():
    global running
    evts = get_events()
    for e in evts:
        if e.type == SDL_QUIT:
            running = False
        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            running = False

open_canvas()

enter()

running = True

while running:
    # event handling
    handle_events()

    # game logic
    update()

    # game rendering
    clear_canvas()
    draw()
    update_canvas()

    delay(0.01)

close_canvas()

