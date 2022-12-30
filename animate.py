import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def animation_setup(ball):
    circle = plt.Circle((ball._pos[0][0],ball._pos[0][1]),ball._radius)

    return circle,

def init():

    return circle,

def animate(i):

    y = ball._pos[i][1]
    x = ball._pos[i][0]

    circle.center = (x,y)

    return circle,

def run_animation(ball):

    fig = plt.figure() 
    circle = animation_setup(ball)

    ax = plt.axes(xlim=(-10, 10), ylim=(-10, 10))
    ax.add_patch(circle)

    ani = animation.FuncAnimation(fig, animate, init_func=init,frames=360, interval=20,blit=True)
    plt.show()

    return
