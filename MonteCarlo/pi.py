import random, math
import matplotlib.pyplot as plt

def fun(x):
    return math.sqrt(1-x*x)

class PiEstimation:
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
            random_num_x = random.random()
            random_num_y = random.random()

            y_real_value = fun(random_num_x)
            if random_num_y <= y_real_value:
                self.inside += 1
            else:
                self.outside += 1
            
            iteration -= 1
    
    def area_approximate(self):
        self.run()
        return (self.inside / (self.inside + self.outside) * 4)

areaFinder = PiEstimation(0, 1, 0, 1, 1000000)
pi_estimated = areaFinder.area_approximate()
print(f"Estimated Pi: {pi_estimated}")

# Simple graph
x_curve = [x/1000 for x in range(0, 1001)]
y_curve = [fun(x) for x in x_curve]

plt.figure(figsize=(8, 8))
plt.plot(x_curve, y_curve, 'b-', linewidth=2, label='Quarter Circle')
plt.fill_between(x_curve, 0, y_curve, alpha=0.2, color='blue')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.gca().set_aspect('equal')
plt.grid(True, alpha=0.3)
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Pi Estimation = {pi_estimated:.5f}')
plt.legend()
plt.show()
