from vpython import *
import numpy as np


def tetrahedron(p1, p2, p3, p4):
    plotTriangle(p1, p2, p3, color.red)
    plotTriangle(p2, p3, p4, color.blue)
    plotTriangle(p3, p4, p1, color.green)
    plotTriangle(p4, p1, p2, color.yellow)


def plotTriangle(tp1, tp2, tp3, triColor):
    tp1 = vertex(pos=vec(tp1[0], tp1[1], tp1[2]), color=triColor)
    tp2 = vertex(pos=vec(tp2[0], tp2[1], tp2[2]), color=triColor)
    tp3 = vertex(pos=vec(tp3[0], tp3[1], tp3[2]), color=triColor)
    triangle(v0=tp1, v1=tp2, v2=tp3)


if __name__ == '__main__':
    tetrahedron(np.array([3, 5, 3]), np.array([-3, 5, 3]), np.array([0, -5, 3]), np.array([0, 0, -3]))
