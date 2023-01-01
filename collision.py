import numpy as np

def collision_check_wall(ball): # (ball, wall)

    wall_x1 = -10
    wall_x2 = 10
    wall_y1 = 0
    wall_y2 = 0

    dot = (((ball._pos[ball._t][0]-wall_x1)*(wall_x2-wall_x1)) \
            + ((ball._pos[ball._t][1]-wall_y1)*(wall_y2-wall_y1))) \
            / (np.linalg.norm([wall_x2-wall_x1,wall_y2-wall_y1]))**2

    closest_x = wall_x1 + (dot * (wall_x2 - wall_x1))
    closest_y = wall_y1 + (dot * (wall_y2 - wall_y1))

    # Check if point is on line (https://www.jeffreythompson.org/collision-detection/line-circle.php)

    dist_x = closest_x - ball._pos[ball._t][0]
    dist_y = closest_y - ball._pos[ball._t][1]

    distance = np.sqrt( dist_x**2 + dist_y**2 )

    return distance <= ball._radius

def collision_check_ball(ball1, ball2):
    return distance_between_balls(ball1, ball2) <= (ball1._radius + ball2._radius)**2

def distance_between_balls(ball1, ball2):
    return (ball1._pos[ball1._t][0]-ball2._pos[ball1._t][0])**2 + (ball1._pos[ball1._t][1]-ball2._pos[ball1._t][1])**2