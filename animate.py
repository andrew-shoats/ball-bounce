import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def setup_animation(fig):
    
    ax = plt.axes(xlim=(-10, 10), ylim=(-10, 10))
    ball_pos = plt.Circle((ball._pos[0][0],ball._pos[0][1]),ball._radius)
    ax.add_patch(ball_pos)

    return ball_pos,


def animate(i, ball_pos):

    y = ball._pos[i][1]
    x = ball._pos[i][0]

    ball_pos.center = (x,y)

    return ball_pos,

def run_animation(ball):
    
    fig = plt.figure("Ball World")
    
    ani = animation.FuncAnimation(
        fig, animate, init_func=setup_animation,frames=360, interval=20,blit=True)
    plt.show()

    return
