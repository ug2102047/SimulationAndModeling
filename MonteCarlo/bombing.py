import random
import matplotlib.pyplot as plt

hit_count = 0
miss_count = 0

for _ in range(1000000):
    x_random = random.uniform(-1.5, 1.5)
    x_val = 500 * x_random
    y_random = random.uniform(-1.5, 1.5)
    y_val = 300 * y_random

    if (abs(x_val) <= 500) and (abs(y_val) <= 300):
        hit_count += 1
    else:
        miss_count += 1

strike_percentage = hit_count / (hit_count + miss_count) * 100
print("Strike Percentage: ", strike_percentage)

# Simple graph for hit and miss counts
labels = ["Hit", "Miss"]
values = [hit_count, miss_count]

plt.bar(labels, values, color=["green", "red"])
plt.title("Bombing Result")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()
