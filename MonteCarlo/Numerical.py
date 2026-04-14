import random
import matplotlib.pyplot as plt

def fun(x):
    return x**3

class NumericalIntegration:
    def __init__(self, range_x_in, range_x_out, range_y_in, range_y_out, iteration=50):
        self.inside = 0
        self.outside = 0
        self.iteration = iteration
        self.range_x_in = range_x_in
        self.range_x_out = range_x_out
        self.range_y_in = range_y_in
        self.range_y_out = range_y_out

    def run(self):
        iteration = self.iteration
        while iteration > 0:
            random_num_x = random.uniform(self.range_x_in, self.range_x_out)
            random_num_y = random.uniform(self.range_y_in, self.range_y_out)

            y_real_value = fun(random_num_x)
            if random_num_y <= y_real_value:
                self.inside += 1
            else:
                self.outside += 1
            
            iteration -= 1
    
    def area_approximate(self):
        self.run()

        rectangle_area = (self.range_x_out - self.range_x_in) * (self.range_y_out - self.range_y_in)
        return (self.inside / (self.inside + self.outside) * rectangle_area)

areaFinder = NumericalIntegration(2, 5, 0, 140, 10000)
estimated_area = areaFinder.area_approximate()
print(f"Estimated Area: {estimated_area}")

# Plot the function and integration region
x_vals = [x for x in range(2, 6)]
y_vals = [fun(x) for x in x_vals]

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, 'b-', linewidth=2, label='f(x) = x³')
plt.fill_between(x_vals, 0, y_vals, alpha=0.3, color='blue', label=f'Area ≈ {estimated_area:.2f}')
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)
plt.grid(True, alpha=0.3)
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.title('Numerical Integration: Area under f(x) = x³ [2, 5]', fontsize=14)
plt.legend(fontsize=11)
plt.show()
