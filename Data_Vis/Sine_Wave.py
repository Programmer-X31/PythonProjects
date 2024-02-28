import numpy as np
from matplotlib import pyplot as plt, style

style.use('ggplot')
time = np.arange(0, 10, 0.1)
wave_sin = [np.sin(element) for element in time]
wave_cos = [np.cos(element) for element in time]
# time_tan = np.arange(0, 10, 0.1)
# wave_tan = [np.tan(element) for element in time_tan]

plt.plot(time, wave_sin)
plt.plot(time, wave_cos)
# plt.plot(time_tan, wave_tan)
plt.show()
