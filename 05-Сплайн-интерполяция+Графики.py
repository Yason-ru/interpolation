import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

x = [1.415, 1.42, 1.425, 1.43, 1.435, 1.44, 1.445]
y = [0.87, 0.88, 0.85, 0.86, 0.89, 0.9, 0.92]

f2 = interp1d(x, y, kind='cubic')   # функция сплайна

x2 = np.linspace(1.415, 1.445, 40)  # 40 точек для функции сплайна в диапазоне [1.415, 1.445]

plt.plot(x,y,'o-', x2, f2(x2),'--') # построение графиков

plt.legend(['линии', 'сплайн'], loc='best')  # название графиков

plt.show()


