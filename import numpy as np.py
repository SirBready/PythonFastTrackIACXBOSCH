import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Especificaciones del filtro
fc = 1000  # Frecuencia de corte en Hz
fs = 8000  # Frecuencia de muestreo en Hz
order = 4  # Orden del filtro

# Diseño del filtro
b, a = signal.butter(order, fc / (fs / 2), btype='low', analog=False, output='ba')

# Respuesta en frecuencia del filtro
w, h = signal.freqz(b, a, fs=fs)

# Gráfico de respuesta en frecuencia
fig, ax = plt.subplots()
ax.plot(w, 20 * np.log10(abs(h)), 'b')
ax.set(title='Respuesta en frecuencia del filtro pasa baja',
       xlabel='Frecuencia [Hz]',
       ylabel='Ganancia [dB]')
ax.grid(True)
plt.show()
