import curses
from simulation import NBodySimulation

# https://css-tricks.com/creating-your-own-gravity-and-space-simulator/

def main(main_screen):
    labels = ['●', '◯', '◌']
    screen = curses.initscr()
    # Get terminal bounds
    max_y, max_x = screen.getmaxyx()
    # Disable blinking cursor
    curses.curs_set(0)
    screen.refresh()
    # Initialise the simulation
    sim = NBodySimulation(w=max_x, h=max_y, dt=0.01, G=40)
    mid_x, mid_y = int(max_x/2), int(max_y/2)
    
    # import random
    # for _ in range(1):
    #     m = random.randint(1, 4)
    #     x = random.randint(-10, 10)
    #     y = random.randint(-15, 15)
    #     vx = random.randint(-25, 25)
    #     vy = random.randint(-25, 25)
    #     sim.create_body(m=m, x=mid_x+x, y=mid_y+y, vx=vx, vy=vy)
    
    # sim.create_body(m=500, x=mid_x, y=mid_y)

    # Sun
    import math
    sim.create_body(m=1000, x=mid_x, y=mid_y)
    orb_v = math.sqrt(40*1000 / 7)
    sim.create_body(m=0.1, x=mid_x+7, y=mid_y+7, vx=orb_v*math.sin(45), vy=-orb_v*math.cos(45))
    # sim.create_body(m=0.5, x=mid_x-10, y=mid_y-10, vx=1, vy=1)

    for state in sim.start():
        i = 0
        for body in state:
            x = int(body['x'])
            y = int(body['y'])
            try:
                screen.addch(y, x, labels[i % len(labels)])
            except curses.error:
                pass
            i += 1 % len(state)
        screen.refresh()
        curses.napms(20)
        screen.clear()
    screen.refresh()
    curses.napms(2000)
    curses.endwin()

curses.wrapper(main)