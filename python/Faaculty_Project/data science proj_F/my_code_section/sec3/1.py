import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 2, 8, 18, 32, 50])
f = interp1d(x, y, kind='cubic')  # استيفاء مكعب

x_new = np.linspace(0, 5, 50)  # نقاط جديدة
y_new = f(x_new)

plt.plot(x, y, 'o', label='Data')  # نقاط البيانات الأصلية
plt.plot(x_new, y_new, '-', label='Interpolated')  # المنحنى المستوفي
plt.legend()
plt.show()
