from vpython import *
import numpy as np


def findPoints(X1, X2, X3):
    # Find the normal of the plane containing three points
    N = np.cross((X2 - X1), (X3 - X1))
    N_normal = N / sqrt(N[0]**2 + N[1]**2 + N[2]**2)
    b = np.dot(N_normal, ((X2 + X1) / 2))  # Offset

    # Find the point of circumcenter
    Xm_12 = X2 - X1
    Xm_23 = X3 - X2

    # L_12 = X_1 + X_12 * t
    # L_23 = X_2 + X_23 * t

    d1 = np.cross(N_normal, Xm_12)
    d2 = np.cross(N_normal, Xm_23)

    node_12 = (X2 + X1) / 2
    node_23 = (X3 + X2) / 2

    points(pos=vec(node_12[0], node_12[1], node_12[2]), radius=5, color=color.red)
    points(pos=vec(node_23[0], node_23[1], node_23[2]), radius=5, color=color.red)

    A = ([d1[0], -d2[0]], [d1[1], -d2[1]])
    contant = [node_23[0] - node_12[0], node_23[1] - node_12[1]]
    A_inv = np.linalg.inv(A)
    st = A_inv.dot(contant)
    X0 = node_12 + d1.dot(st[0])
    points(pos=[vec(X0[0], X0[1], X0[2])], radius=5, color=color.red)
    arrow(pos=vec(node_12[0], node_12[1], node_12[2]), axis=vec(d1[0], d1[1], d1[2]), color=color.blue, shaftwidth=0.05)
    arrow(pos=vec(node_23[0], node_23[1], node_23[2]), axis=vec(d2[0], d2[1], d2[2]), color=color.blue, shaftwidth=0.05)
    arrow(pos=vec(X0[0], X0[1], X0[2]), axis=vec(N_normal[0], N_normal[1], N_normal[2]) * 10, color=color.orange, shaftwidth=0.05)
    arrow(pos=vec(X0[0], X0[1], X0[2]), axis=vec(-N_normal[0], -N_normal[1], -N_normal[2]) * 10, color=color.orange, shaftwidth=0.05)
    equation = np.poly1d([N_normal[0]**2 + N_normal[1]**2 + N_normal[2]**2, -(2 * (X0[0] - X1[0]) * N_normal[0] + 2 * (X0[1] - X1[1]) * N_normal[1] + 2 * (X0[2] - X1[2]) * N_normal[2]), (X1[0] - X0[0]) ** 2 + (X1[1] - X0[1]) ** 2 + (X1[2] - X0[2]) ** 2 - 100])
    ans_t = (equation.r)
    ans_1 = X0 + N_normal.dot(ans_t[0])
    ans_2 = X0 + N_normal.dot(ans_t[1])
    points(pos=[vec(ans_1[0], ans_1[1], ans_1[2])], radius=5, color=color.yellow)
    points(pos=[vec(ans_2[0], ans_2[1], ans_2[2])], radius=5, color=color.yellow)

    # Plot three points as a triangle
    y = plotTriangle(X1, X2, X3)

    # Plot 3 axes
    X_axis = arrow(pos=vec(0, 0, 0), axis=vec(10, 0, 0), color=color.cyan, shaftwidth=0.05)
    Y_axis = arrow(pos=vec(0, 0, 0), axis=vec(0, 10, 0), color=color.cyan, shaftwidth=0.05)
    Z_axis = arrow(pos=vec(0, 0, 0), axis=vec(0, 0, 10), color=color.cyan, shaftwidth=0.05)
    X_axisText = text(pos=vec(11, 0, 0), text='x', align='center', color=color.green)
    Y_axisText = text(pos=vec(0, 11, 0), text='y', align='center', color=color.green)
    Z_axisText = text(pos=vec(0, 0, 11), text='z', align='center', color=color.green)


def plotTriangle(tp1, tp2, tp3):
    # Plot four triangles to become tetrahedron
    tp1 = vertex(pos=vec(tp1[0], tp1[1], tp1[2]))
    tp2 = vertex(pos=vec(tp2[0], tp2[1], tp2[2]))
    tp3 = vertex(pos=vec(tp3[0], tp3[1], tp3[2]))
    triangle(v0=tp1, v1=tp2, v2=tp3)


if __name__ == '__main__':
    findPoints(np.array([3, 5, 3]), np.array([4, 7, 8]), np.array([8, 3, 6]))
