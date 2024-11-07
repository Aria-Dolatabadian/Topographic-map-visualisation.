import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
data_loaded = pd.read_csv('topography_data.csv')

# Extract the columns after loading the data
x_loaded = data_loaded['X'].values.reshape(100, 100)
y_loaded = data_loaded['Y'].values.reshape(100, 100)
z_loaded = data_loaded['Z'].values.reshape(100, 100)

# Plot the topographic data using contour and color shading
fig, ax = plt.subplots(figsize=(10, 8))
contour = ax.contourf(x_loaded, y_loaded, z_loaded, cmap='terrain', levels=20)
contour_lines = ax.contour(x_loaded, y_loaded, z_loaded, colors='black', linewidths=0.5, levels=20)
fig.colorbar(contour, ax=ax, label='Elevation')

# Add labels and title
ax.set_xlabel('X Coordinate')
ax.set_ylabel('Y Coordinate')
ax.set_title('Topographic Map Simulation')

# Show the plot
plt.show()

# Plot the topographic data in 3D
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Use a surface plot to display the topography
surf = ax.plot_surface(x_loaded, y_loaded, z_loaded, cmap='terrain', edgecolor='k', linewidth=0.1)

# Add a color bar for elevation
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, label='Elevation')

# Customize the plot
ax.set_xlabel('X Coordinate')
ax.set_ylabel('Y Coordinate')
ax.set_zlabel('Elevation')
ax.set_title('3D Topographic Map Simulation')

# Show the plot
plt.show()
