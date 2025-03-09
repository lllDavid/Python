import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperature = [22, 24, 26, 27, 25, 23, 22]

plt.plot(days, temperature, marker='o')
plt.title('Temperature over the Week')
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()
