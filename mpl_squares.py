import matplotlib as mpl
import matplotlib.pyplot as plt

x_values = range(1, 100)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-darkgrid')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=mpl.colormaps['Blues'], s=10)
# ax.plot(x_values, y_values, linewidth=3)

# Set chart title and label axes.
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

# Set the range of each axis.
ax.axis([0, 110, 0, 11000])

plt.show()