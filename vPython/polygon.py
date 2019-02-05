from matplotlib import pyplot
import numpy as np
from math import sqrt


def offsetPolygon(polypoints, delta):

    poly = list(polypoints)
    v = []
    vNormalized = []
    sinAlpha = []
    new_point = []
    pointsNumber = len(polypoints)
    poly.extend([polypoints[0]])
    print('Points:', poly)

    for i in range(pointsNumber):
        v.append(poly[i + 1] - poly[i])
    v.append(v[0])
    print('v:\n', v)

    for i in range(len(v)):
        vNormalized.append(v[i] / sqrt(pow(v[i][0], 2) + pow(v[i][1], 2)))
    print('vNormalized:\n', vNormalized)

    for i in range(pointsNumber):
        sinAlpha.append(abs(np.cross(v[i], v[i + 1])) / (sqrt(pow(v[i][0], 2) + pow(v[i][1], 2)) * sqrt(pow(v[i + 1][0], 2) + pow(v[i + 1][1], 2))))
    print('sinAlpha:\n', sinAlpha)

    for i in range(pointsNumber):
        new_point.append(poly[i + 1] + (delta / sinAlpha[i]) * ((vNormalized[i + 1] - vNormalized[i])))
    print('New points:\n', new_point)

    # Plot offset polygon
    x_new = [x[0] for x in new_point]
    x_new.extend([new_point[0][0]])

    y_new = [y[1] for y in new_point]
    y_new.extend([new_point[0][1]])

    fig = pyplot.figure(1, figsize=(5, 5), dpi=90)
    ax = fig.add_subplot(111)
    ax.plot(x_new, y_new)

    # Plot the orginal polygon
    x_val = [x[0] for x in polypoints]
    x_val.extend([polypoints[0][0]])
    y_val = [x[1] for x in polypoints]
    y_val.extend([polypoints[0][1]])

    ax.plot(x_val, y_val)
    pyplot.gca().set_aspect('equal', adjustable='box')
    pyplot.show()


if __name__ == '__main__':
    # offsetPolygon(np.array([(0, 0), (4, 0), (5, 2), (4, 5), (2, 3)]), 1.0)
    # offsetPolygon(np.array([(0, 0), (4, 0), (2, 2 * sqrt(3))]), 1.0)
    # offsetPolygon(np.array([(0, 0), (3, 0), (4, 3), (1.5, 5), (-2, 3)]), 1.0)
    offsetPolygon(np.array([(0, 0), (6, 0), (6, 8)]), 1.0)
