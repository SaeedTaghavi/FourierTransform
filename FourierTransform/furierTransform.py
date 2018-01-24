from scipy.fftpack import fft
import numpy as np
# Number of sample points
N = 1000
# sample spacing
T = 1.0 / 500.0
x = np.linspace(0.0, N*T, N)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(165.0 * 2.0*np.pi*x)
noise = np.random.rand(N)
y = y+noise
yf = fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)

import matplotlib.pyplot as plt
plt.plot(x,y)
plt.show()
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.grid()
plt.show()
