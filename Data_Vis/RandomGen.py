from matplotlib import pyplot as plt
import numpy as np

data_x = []
data_y = []
for i in range(1,361):
    data_y.append(np.sin(i))
    data_x.append(i)


plt.plot(data_y, data_x)
plt.show()

