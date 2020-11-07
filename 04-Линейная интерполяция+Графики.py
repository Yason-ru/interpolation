import matplotlib.pyplot as plt

x = [1.415, 1.42, 1.425, 1.43, 1.435, 1.44, 1.445]
y = [0.87, 0.88, 0.85, 0.86, 0.89, 0.9, 0.92]

xk = 1.428  # при этом x найти y
i = 0
while xk > x[i]:
    i = i + 1

yk = y[i-1] + (y[i] - y[i-1])*(xk - x[i-1])/(x[i] - x[i-1])
print('xk=', xk, 'yk=', yk)

plt.plot(x,y,'r--', xk,yk,'b*')

plt.show()

