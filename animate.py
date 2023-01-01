import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Animate_Ball:

    def __init__(self, ball_vector):
        self.fig = plt.figure()
        self.ax = plt.axes(xlim=(-10, 10), ylim=(0, 30))
        self.circle_vector = []
        self.data_vector = []
        for ball in ball_vector:
            self.circle_vector.append(plt.Circle(([],[]),ball._radius))
            self.data_vector.append(ball._pos)

    def init_anim(self):
        for idx, circle in enumerate(self.circle_vector):
            circle.center = (self.data_vector[idx][0][0], self.data_vector[idx][0][1])
            self.ax.add_patch(circle)
        return tuple(self.circle_vector)
        #return self.circle,

    def update(self, i):
        for idx, circle in enumerate(self.circle_vector):
            
            x = self.data_vector[idx][i*5][0]
            y = self.data_vector[idx][i*5][1]

            circle.center = (x, y)

        return tuple(self.circle_vector)

    def animate(self):
        ani = animation.FuncAnimation(self.fig, self.update, init_func=self.init_anim,
              blit=True)

        #plt.axis('scaled')
        plt.show()
