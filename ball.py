import numpy as np
import collision as colli

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
        self._obstacles = []

    def update_obstacles(self, obstacles):
        for obstacle in obstacles:
            self._obstacles.append(obstacle)

    def update_pos(self):
        pos = self._pos[self._t]
        x = pos[0]
        y = pos[1]

        vel = self._vel[self._t]
        vx = vel[0]
        vy = vel[1]

        collision_misses = 0

        for obstacle in self._obstacles:
            if colli.collision_check_wall(self):
                vx += 0
                vy = -self.inelastic_collision(5) # This may occur more than once? Need to check on
            elif colli.collision_check_ball(self, obstacle):
                vx += 0
                vy = -self.inelastic_collision(obstacle)
            else:
                if collision_misses == 0:
                    vx += 0
                    vy += -9.81 * self._dt
                    collision_misses += 1
                else:
                    collision_misses += 1

        x += 0
        y += self._dt * vy

        self._vel.append([vx,vy])
        self._pos.append([x,y])

        self._t += 1

        return
        
    def inelastic_collision(self, obstacle): #(self, object (wall or another ball)) # 1D
        if type(obstacle) == Ball:
            c_r = 0.99
            m_b = obstacle._mass
            u_b = obstacle._vel[obstacle._t][1]
        else:
            c_r = 0.5
            m_b = 1_000_000 # wall
            u_b = 0

        return (c_r * m_b * self._vel[self._t][1]+self._mass * self._vel[self._t][1] + m_b * u_b)/(m_b + self._mass)