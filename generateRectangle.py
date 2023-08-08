import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Define the coordinates of the rectangle's corners
x = [1, 3, 3, 1, 1]  # x-coordinates of the four corners
y = [2, 2, 4, 4, 2]  # y-coordinates of the four corners

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the rectangle
ax.plot(x, y, marker='o')  # Use marker='o' to plot vertices as circles

# Set axis limits
ax.set_xlim(min(x) - 1, max(x) + 1)
ax.set_ylim(min(y) - 1, max(y) + 1)

# Set axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Add grid lines
ax.grid(True)

# Add title
ax.set_title('Rectangle on Cartesian Coordinates')

# Show the plot
plt.savefig('grafico.png')
plt.imshow('X')