import numpy as np
import matplotlib  # need this line when using virtaulenv
matplotlib.use('TkAgg')  # need this line when using virtaulenv
import matplotlib.pyplot as plt
plt = matplotlib.pyplot

X = [590, 540, 740, 130, 810, 300, 320, 230, 470, 620, 770, 250]
Y = [32, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]

a = np.arange(0, 1000)
b = np.sin(a * np.pi / 180.0)

plt.subplot(121)
plt.plot(a, b, "y--", lw=3)
plt.xlim(0, 1000)
plt.ylim(-2, 2)
plt.title('Sin() function')
plt.xlabel('Angel')
plt.ylabel('Value')

plt.subplot(122)
# scatter plot
plt.scatter(X, Y, s=60, c='red', marker='.')

# change axes ranges
plt.xlim(0, 1000)
plt.ylim(0, 100)

# add title
plt.title('CP prediction in Pokémon Go')

# add x and y labels
plt.xlabel('Current CP')
plt.ylabel('Predicted CP')

# show plot
plt.show()
