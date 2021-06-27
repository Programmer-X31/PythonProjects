from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [0, 400, 800, 1200, 1600, 2000]
y = [num * 10 for num in range(6)]
x2 = [4000, 3200, 2400, 1600, 800, 0]

plt.plot(x, y)
plt.plot(x2, y)
plt.show()
