import matplotlib.pyplot as plt
import numpy as np

def setup_animation(ball):

    plt.figure("Ball World")
    plt.xlim([-10,10])
    plt.ylim([-10,10])
    
    # Would be from ball object
    t = np.linspace(0, 2 * np.pi, 100)
    r = 3
    y = r*np.sin(t)
    x = r*np.cos(t)

    plt.plot(x,y)
    plt.show()
