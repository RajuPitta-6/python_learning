import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 20, 25, 30]

# Custom line style
plt.plot(x, y, color='red', linestyle='--', linewidth=3, marker='o', markersize=8, markerfacecolor='yellow')

plt.title("Customized Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()

# Grid and Background
x = [1, 2, 3, 4, 4, 5]
y = [2, 4, 6, 8, 7, 9]

plt.plot(x, y, color='purple', marker='s')
plt.title("Grid Example")
plt.xlabel("X")
plt.ylabel("Y")

# Add grid
plt.grid(True, linestyle=':', linewidth=1, color='gray')
plt.show()

# Adding Annotations (Text on Graph)
x = [1, 2, 3, 4, 5]
y = [2, 4, 8, 16, 32]

plt.plot(x, y, marker='o', color='green')
plt.title("Annotation Example")
plt.xlabel("X")
plt.ylabel("Y")

# Annotate point (4,16)
plt.annotate("Important Point", xy=(4, 16), xytext=(2, 20),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.show()


# Figure Size & Font Customization-----------
plt.figure(figsize=(8,5))  # width, height in inches

x = [1, 2, 3, 4, 5]
y = [10, 12, 15, 20, 25]

plt.plot(x, y, color='orange', marker='^', linewidth=3)
plt.title("Custom Figure Size Example", fontsize=16, fontweight='bold')
plt.xlabel("X Axis", fontsize=12)
plt.ylabel("Y Axis", fontsize=12)
plt.grid(True)

plt.show()

# Style Sheets (Preset Themes)-------------------------

# Apply a style
plt.style.use('seaborn-v0_8-darkgrid')

x = [1, 2, 3, 4, 5]
y = [3, 8, 1, 10, 5]

plt.plot(x, y, marker='o', linewidth=2)
plt.title("Styled Plot Example")
plt.show()

# Save Customized Plot----------------
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 18, 20]

plt.plot(x, y, color='blue', marker='o')
plt.title("Customized Saved Plot", fontsize=14)
plt.grid(True)
plt.savefig("customized_plot_day3.png", dpi=300, bbox_inches='tight')
plt.show()
