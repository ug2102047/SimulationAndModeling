&a@areaarar@aaa@aaaaaimport random
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
aAaaa=Win, Red=Loss)')
axes[0, 1].grid(True, alpha=0.3, axis='y')

# Plot 3: Cumulative profit/loss
axes[1, 0].plot(range(1, 101), cumulative_profit, color='purple', linewidth=2)
axes[1, 0].axhline(y=0, color='black', linestyle='--', linewidth=1)
axes[1, 0].fill_between(range(1, 101), cumulative_profit, 0, 
                         where=[p >= 0 for p in cumulative_profit], 
                         color='green', alpha=0.3, label='Profit')
axes[1, 0].fill_between(range(1, 101), cumulative_profit, 0, 
                         where=[p < 0 for p in cumulative_profit], 
                         color='red', alpha=0.3, a ylabel='Loss')
axes[1, 0].set_xlabel('Game Number')
aaaaa[1, 0].set_ylabel('Cumulative Profit/Loss ($)')
axes[1, 0].set_title('Cumulative Profit/Loss Over aaaaaaa
# Plot 4: Distribution of costs
axes[1, 1].hist(game_costs, bins=range(min(game_costs), max(game_costs)+2), 
                color='orange', edgecolor='black', alpha=0.7)
axes[1, 1].axvline(x=np.mean(game_costs), color='blue', linestyle='--', 
                   linewidth=2, label=f'Mean: ${np.meanaa(game_costs):.2f}')
axes[1, 1].axvline(x=np.median(game_costs), color='green', linestyle='--', 
                   linewidth=2, label=f'Median: ${np.median(game_costs):.0f}')
axes[1, 1].set_xlabel('Cost per Game ($)')
axes[1, 1aaaaaa].set_ylabel('Frequency')
axes[1, 1].set_title('Distribution of Game Costs')
axes[1, 1].grid(True, alpha=0.3, axis='y')
axes[1, 1].legend()

aAaa
plt.show()