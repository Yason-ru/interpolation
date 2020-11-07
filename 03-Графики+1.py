# pip install numpy
# pip install matplotlib
#Если ошибка =  'ft2font: Не найден указанный модуль' ТО
    #pip uninstall matplotlib
    #pip install -U matplotlib==3.2.0rc1

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(-x) * np.cos(2*np.pi*x)

x1 = np.arange(0.0, 5.0, 0.1)
x2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)

plt.subplot(211)
plt.plot(x1, f(x1), 'bo', x2, f(x2), 'k')

plt.subplot(212)
plt.plot(x2, np.cos(2*np.pi*x2), 'r--')

plt.show()