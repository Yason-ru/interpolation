x = [1,2,3,4,5,6]
y = [3,2,4,1,3,5]

n = len(x)    # кол-во точек

xk = 2.4  # при этом x найти y

i = 0
while xk > x[i]: # определение диапазона [x[i-1], x[i]], куда попадает xk
    i = i + 1
print('x[i-1]=', x[i-1], 'x[i]=', x[i])

yk = y[i-1] + (y[i] - y[i-1])*(xk - x[i-1])/(x[i] - x[i-1])

print('Ответ. При xk=', xk, 'yk=', yk)

###########################################################

x = [1.415, 1.42, 1.425, 1.43, 1.435, 1.44, 1.445]
y = [0.87, 0.88, 0.85, 0.86, 0.89, 0.9, 0.92]

xk = 1.428  # при этом x найти y

i = 0
while xk > x[i]: # определение диапазона [x[i-1], x[i]], куда попадает xk
    i = i + 1
print('x[i-1]=', x[i-1], 'x[i]=', x[i])

yk = y[i-1] + (y[i] - y[i-1])*(xk - x[i-1])/(x[i] - x[i-1])

print('Ответ. При xk=', xk, 'yk=', yk)

