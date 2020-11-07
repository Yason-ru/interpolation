# pip install numpy
# pip install matplotlib
#Если ошибка =  'ft2font: Не найден указанный модуль' ТО
    #pip uninstall matplotlib
    #pip install -U matplotlib==3.2.0rc1

import numpy as np
import matplotlib.pyplot as plt
import math

x = [1,2,3,4]
y = [3,2,1,4]

x1 = np.arange(0,5,0.1)  # 0.1 - шаг
y1 = np.sin(math.pi*x1)

plt.plot(x,y,'r--', x1,y1,'b--')

plt.show()

