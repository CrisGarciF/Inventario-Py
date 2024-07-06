import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)

y = np.log(x**2 + 1) - x / 10

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfica del Punto 2')
plt.show()


#Punto 3

import numpy as np
import matplotlib.pyplot as plt

x = [-4, 4, 4, 4, -4, -4]
y = [-4, -4, 4, 4, 4, -4]

fig, tmax = plt.subplots()
tmax.plot(x, y)

color = ['red', 'blue', 'green', 'orange', 'purple', 'yellow']
for i in range(len(x)):
  tmax.add_patch(plt.Circle((x[i], y[i]), 1.0, fill=False, edgecolor=color[i]))

x = np.linspace(-1, 1, 1000) * np.pi
plt.plot(np.cos(x), np.sin(x))

tmax.set_xlim(-6, 6)
tmax.set_ylim(-6, 6)

plt.show()