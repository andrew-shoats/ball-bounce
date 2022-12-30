import numpy as np

class Ball:
    
    def __init__(self, radius, mass, x0, y0):
        self._x0 = [x0,y0]
        self._pos = [self._x0]
        self._v0 = [0,0]
        self._vel = [self._v0]
        self._radius = radius
        self._mass = mass
        self._t = 0
        self._dt = 0.01
        self._ball_shape = []

    def update_pos(self):
        pos = self._pos[self._t]
        x = pos[0]
        y = pos[1]

        vel = self._vel[self._t]
        vx = vel[0]
        vy = vel[1]

        self._t += 1

        vx += 0
        vy += -9.81 * self._dt

        x += 0
        y += self._dt * vy

        self._vel.append([vx,vy])
        self._pos.append([x,y])

        self.update_ball_shape()

        return

    def update_ball_shape(self):

        s = np.linspace(0, 2 * np.pi, 100)
        y = self._radius*np.sin(s) + self._pos[self._t][1]
        x = self._radius*np.cos(s) + self._pos[self._t][0]
        self._ball_shape.append([x,y])

        return
        