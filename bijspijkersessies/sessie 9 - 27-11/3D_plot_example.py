import seaborn as seaborn
import matplotlib.pyplot as plot
import numpy as np

seaborn.set_style("darkgrid")

mean = 3
number = 50

x1 = np.random.normal(mean, 1, size=number)
y1 = np.random.normal(mean, 1, size=number)
z1 = np.random.normal(mean, 1, size=number)
c = np.random.choice(["blue", "orange"], size=number)
print(c)

plot.figure(figsize=(6, 5))
axes = plot.axes(projection="3d")
print(type(axes))
axes.scatter3D(x1, y1, z1, c=c)

axes.set_xlabel("x")
axes.set_ylabel("y")
axes.set_zlabel("z")
plot.show()