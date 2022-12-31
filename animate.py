import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class Animate_Ball:

    def __init__(self, ball):
        self.fig = plt.figure()
        self.ax = plt.axes(xlim=(-10, 10), ylim=(-10, 10))
        self.circle = plt.Circle(([],[]),ball._radius)
        self.data = ball._pos

    def set_ball_path(self):
        self.data_x = self.data[0]
        self.data_y = self.data[1]

    def init_anim(self):
        self.circle.center = (self.data[0][0], self.data[0][1])
        self.ax.add_patch(self.circle)
        return self.circle,

    def update(self, i):
        x = self.data[i][0]
        y = self.data[i][1]

        self.circle.center = (x, y)

        return self.circle,

    def animate(self):
        ani = animation.FuncAnimation(self.fig, self.update, init_func=self.init_anim,
              blit=True)

        plt.show()
