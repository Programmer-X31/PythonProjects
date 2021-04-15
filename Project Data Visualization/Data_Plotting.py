from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

y = [3, 10, 5, 16, 8, 4, 2, 1]
x = [num * 1 for num in range(1, (len(y) + 1), 1)]

plt.plot(x, y)
plt.title('Collatz Sequence')
plt.xlabel('Collatz No')
plt.ylabel('No of steps')
plt.show()