import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

total_cost = 0
total_income = 0
game_costs = []
game_profits = []
cumulative_profit = []

for game in range(100):
    x = 0
    h = 0
    t = 0
    while(1):
        x += 1
        total_cost += 1
        r = random.randint(0,9)
        if (r < 5):
            h += 1
        else:
            t += 1
        dif = abs(h-t)

        if(dif >= 3):
            print(f"Game {game+1}: Won $8, Cost ${x}")
            total_income += 8
            game_costs.append(x)
            profit = 8 - x
            game_profits.append(profit)
            cumulative_profit.append(total_income - total_cost)
            break

print(f'\nTotal Cost: ${total_cost}')
print(f'Total Income: ${total_income}')
print(f'Net Profit/Loss: ${total_income - total_cost}')
print(f'Average Cost per Game: ${total_cost/100:.2f}')

# Create visualization
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Gambling Game Analysis (100 Games)', fontsize=16, fontweight='bold')

# Plot 1: Cost per game
axes[0, 0].plot(range(1, 101), game_costs, color='red', marker='o', markersize=3, linewidth=1)
axes[0, 0].axhline(y=np.mean(game_costs), color='blue', linestyle='--', label=f'Average: ${np.mean(game_costs):.2f}')
axes[0, 0].set_xlabel('Game Number')
axes[0, 0].set_ylabel('Cost ($)')
axes[0, 0].set_title('Cost per Game')
axes[0, 0].grid(True, alpha=0.3)
axes[0, 0].legend()

# Plot 2: Profit/Loss per game
colors = ['green' if p > 0 else 'red' for p in game_profits]
axes[0, 1].bar(range(1, 101), game_profits, color=colors, alpha=0.7)
axes[0, 1].axhline(y=0, color='black', linestyle='-', linewidth=0.5)
axes[0, 1].set_xlabel('Game Number')
axes[0, 1].set_ylabel('Profit/Loss ($)')
axes[0, 1].set_title('Profit/Loss per Game (Green=Win, Red=Loss)')
axes[0, 1].grid(True, alpha=0.3, axis='y')

# Plot 3: Cumulative profit/loss
axes[1, 0].plot(range(1, 101), cumulative_profit, color='purple', linewidth=2)
axes[1, 0].axhline(y=0, color='black', linestyle='--', linewidth=1)
axes[1, 0].fill_between(range(1, 101), cumulative_profit, 0, 
                         where=[p >= 0 for p in cumulative_profit], 
                         color='green', alpha=0.3, label='Profit')
axes[1, 0].fill_between(range(1, 101), cumulative_profit, 0, 
                         where=[p < 0 for p in cumulative_profit], 
                         color='red', alpha=0.3, label='Loss')
axes[1, 0].set_xlabel('Game Number')
axes[1, 0].set_ylabel('Cumulative Profit/Loss ($)')
axes[1, 0].set_title('Cumulative Profit/Loss Over Time')
axes[1, 0].grid(True, alpha=0.3)
axes[1, 0].legend()

# Plot 4: Distribution of costs
axes[1, 1].hist(game_costs, bins=range(min(game_costs), max(game_costs)+2), 
                color='orange', edgecolor='black', alpha=0.7)
axes[1, 1].axvline(x=np.mean(game_costs), color='blue', linestyle='--', 
                   linewidth=2, label=f'Mean: ${np.mean(game_costs):.2f}')
axes[1, 1].axvline(x=np.median(game_costs), color='green', linestyle='--', 
                   linewidth=2, label=f'Median: ${np.median(game_costs):.0f}')
axes[1, 1].set_xlabel('Cost per Game ($)')
axes[1, 1].set_ylabel('Frequency')
axes[1, 1].set_title('Distribution of Game Costs')
axes[1, 1].grid(True, alpha=0.3, axis='y')
axes[1, 1].legend()

plt.tight_layout()
plt.show() 
