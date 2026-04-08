 import math
import random
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch
from matplotlib.collections import LineCollection 
 
# Random Walk Simulation Parameters
num_simulations = 5  # Number of random walks to simulate
num_steps = 50  # Number of steps in each walk

# Probabilities: Forward, Left, Right, Backward
probabilities = [0.5, 0.2, 0.2, 0.1]
prob_cumulative = [sum(probabilities[:i+1]) for i in range(len(probabilities))]

# Direction mappings
directions_map = {
    'F': (0, 1, 'Forward', '↑'),
    'L': (-1, 0, 'Left', '←'),
    'R': (1, 0, 'Right', '→'),
    'B': (0, -1, 'Backward', '↓')
}

# Storage for all simulations
all_walks = []
all_directions = []
final_distances = []

# Run multiple simulations
print("\n" + "="*70)
print("RANDOM WALK SIMULATION")
print("="*70)
print(f"Number of simulations: {num_simulations}")
print(f"Steps per simulation: {num_steps}")
print(f"Probabilities - Forward: {probabilities[0]}, Left: {probabilities[1]}, Right: {probabilities[2]}, Backward: {probabilities[3]}")
print("="*70)

for sim in range(num_simulations):
    x, y = 0, 0
    path_x = [0]
    path_y = [0]
    directions = []
    
    for step in range(num_steps):
        rn = random.random()  # Generate random number between 0 and 1
        
        # Determine direction based on probability
        if rn < prob_cumulative[0]:
            direction = 'F'
        elif rn < prob_cumulative[1]:
            direction = 'L'
        elif rn < prob_cumulative[2]:
            direction = 'R'
        else:
            direction = 'B'
        
        # Update position
        dx, dy, _, _ = directions_map[direction]
        x += dx
        y += dy
        
        path_x.append(x)
        path_y.append(y)
        directions.append(direction)
    
    all_walks.append((path_x, path_y))
    all_directions.append(directions)
    
    # Calculate final distance from origin
    final_distance = math.sqrt(x**2 + y**2)
    final_distances.append(final_distance)
    
    print(f"Walk {sim+1}: Final position ({x}, {y}), Distance from origin: {final_distance:.2f}")

print("="*70)
print(f"Average final distance: {np.mean(final_distances):.2f}")
print(f"Max distance: {max(final_distances):.2f}")
print(f"Min distance: {min(final_distances):.2f}")
print("="*70)

# ============== VISUALIZATION ==============
fig = plt.figure(figsize=(18, 10))
gs = fig.add_gridspec(2, 3, hspace=0.3, wspace=0.3)

# Color map for different walks
colors = plt.cm.tab10(np.linspace(0, 1, num_simulations))

# Plot 1: All Random Walks (Main Plot)
ax1 = fig.add_subplot(gs[:, :2])
for i, (path_x, path_y) in enumerate(all_walks):
    # Create gradient color effect along the path
    points = np.array([path_x, path_y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    
    # Plot the path
    ax1.plot(path_x, path_y, '-', color=colors[i], linewidth=2, 
             alpha=0.7, label=f'Walk {i+1}')
    
    # Mark start point
    ax1.plot(path_x[0], path_y[0], 'o', color='green', markersize=15, 
             markeredgecolor='black', markeredgewidth=2, zorder=10)
    
    # Mark end point
    ax1.plot(path_x[-1], path_y[-1], 's', color=colors[i], markersize=12, 
             markeredgecolor='black', markeredgewidth=2, zorder=10)
    
    # Add arrow showing direction at end
    if len(path_x) > 1:
        ax1.annotate(f'End {i+1}', xy=(path_x[-1], path_y[-1]), 
                    xytext=(10, 10), textcoords='offset points',
                    fontsize=9, fontweight='bold',
                    bbox=dict(boxstyle='round,pad=0.3', facecolor=colors[i], alpha=0.7))

# Mark origin
ax1.plot(0, 0, 'o', color='green', markersize=20, markeredgecolor='black', 
         markeredgewidth=3, zorder=11, label='Start (Origin)')
ax1.text(0, 0, 'START', ha='center', va='center', fontsize=10, 
         fontweight='bold', color='white')

ax1.set_xlabel('X Position', fontsize=14, fontweight='bold')
ax1.set_ylabel('Y Position', fontsize=14, fontweight='bold')
ax1.set_title('2D Random Walk Paths', fontsize=16, fontweight='bold')
ax1.legend(loc='best', fontsize=10)
ax1.grid(True, alpha=0.3, linestyle='--')
ax1.axhline(y=0, color='k', linestyle='-', linewidth=0.5, alpha=0.5)
ax1.axvline(x=0, color='k', linestyle='-', linewidth=0.5, alpha=0.5)
ax1.set_aspect('equal', adjustable='box')

# Plot 2: Distance from Origin over Time
ax2 = fig.add_subplot(gs[0, 2])
for i, (path_x, path_y) in enumerate(all_walks):
    distances = [math.sqrt(x**2 + y**2) for x, y in zip(path_x, path_y)]
    ax2.plot(range(len(distances)), distances, '-o', color=colors[i], 
             linewidth=2, markersize=3, alpha=0.7, label=f'Walk {i+1}')

ax2.set_xlabel('Step Number', fontsize=12, fontweight='bold')
ax2.set_ylabel('Distance from Origin', fontsize=12, fontweight='bold')
ax2.set_title('Distance from Origin vs Steps', fontsize=13, fontweight='bold')
ax2.legend(fontsize=9)
ax2.grid(True, alpha=0.3)

# Plot 3: Direction Distribution
ax3 = fig.add_subplot(gs[1, 2])
all_dirs_combined = [d for dirs in all_directions for d in dirs]
dir_counts = {
    'Forward': all_dirs_combined.count('F'),
    'Left': all_dirs_combined.count('L'),
    'Right': all_dirs_combined.count('R'),
    'Backward': all_dirs_combined.count('B')
}

# Expected counts based on probabilities
expected_counts = {
    'Forward': probabilities[0] * num_steps * num_simulations,
    'Left': probabilities[1] * num_steps * num_simulations,
    'Right': probabilities[2] * num_steps * num_simulations,
    'Backward': probabilities[3] * num_steps * num_simulations
}

x_pos = np.arange(len(dir_counts))
actual_values = list(dir_counts.values())
expected_values = list(expected_counts.values())

width = 0.35
bars1 = ax3.bar(x_pos - width/2, actual_values, width, label='Actual', 
                color='#3498db', edgecolor='black', linewidth=1.5)
bars2 = ax3.bar(x_pos + width/2, expected_values, width, label='Expected', 
                color='#e74c3c', edgecolor='black', linewidth=1.5, alpha=0.7)

# Add value labels
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}',
                ha='center', va='bottom', fontsize=9, fontweight='bold')

ax3.set_xlabel('Direction', fontsize=12, fontweight='bold')
ax3.set_ylabel('Count', fontsize=12, fontweight='bold')
ax3.set_title('Direction Distribution', fontsize=13, fontweight='bold')
ax3.set_xticks(x_pos)
ax3.set_xticklabels(['Forward ↑', 'Left ←', 'Right →', 'Backward ↓'])
ax3.legend(fontsize=10)
ax3.grid(True, axis='y', alpha=0.3)

# Overall title
fig.suptitle(f'Random Walk Analysis - {num_simulations} Walks × {num_steps} Steps', 
             fontsize=18, fontweight='bold', y=0.98)

plt.savefig('random_walk_simulation.png', dpi=150, bbox_inches='tight')
plt.show()

print("\nVisualization saved as 'random_walk_simulation.png'")
