import matplotlib.pyplot as plt
import numpy as np 

t = np.linspace(0,2*np.pi,101)
y = np.cos(2*t) 
y1 = np.sin(2*t)

plt.figure("Cosseno", figsize=(6,5))
plt.plot (t,y)
plt.title("Gráfico do Cosseno")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude (cos)")

plt.figure(2)
plt.plot (t,y1)
plt.title("Gráfico do Seno")
plt.xlabel("Tempo  (s)")
plt.ylabel("Amplitude 2 (cos)")
plt.show() 