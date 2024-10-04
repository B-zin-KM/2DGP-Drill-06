from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

running = True
cx, cy = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
sx , sy = x, y
frame = 0
t = 0
dir = 0

def rand_cursor():
    global cx, cy, sx, sy, t
    sx = cx
    sy = cy
    cx, cy = random.randint(30, TUK_WIDTH - 30), random.randint(30, TUK_HEIGHT - 30)
    t = 0

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    x = (1 - t) * sx + t * cx
    y = (1 - t) * sy + t * cy
    if sx < cx:
        dir = 1
    else: dir = 0
    t += 0.01
    if t >= 1:
        rand_cursor()
    if dir == 1:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    if dir == 0:
        character.clip_composite_draw(frame * 100, 100 * 1, 100, 100, 0, 'h', x, y, 100, 100)
    cursor.draw(cx, cy)
    update_canvas()
    frame = (frame + 1) % 8
    delay (0.01)
    handle_events()

close_canvas()