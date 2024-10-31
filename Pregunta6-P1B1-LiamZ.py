import numpy as np
def f(x):
    return x**2 - 6*x + 5
a, b = 2, 3
paso = 0.1
intervalosInvalidos = []
valorX = np.arange(a, b, paso)
for i in range(len(valorX) - 1):
    x1 = valorX[i]
    x2 = valorX[i + 1]
    if np.sign(f(x1)) == np.sign(f(x2)):
        intervalosInvalidos.append((round(x1, 1), round(x2, 1)))
print("Intervalos donde f(a) y f(b) tienen el mismo signo:")
for inter in intervalosInvalidos:
    print(inter)