import random
import matplotlib.pyplot as plt 

class RandomWalk3D:
    def __init__(self, step_limit=100):
        self.x_pos = 0
        self.y_pos = 0
        self.z_pos = 0
        self.step_limit = step_limit
        self.history = [(self.x_pos, self.y_pos, self.z_pos)]
    
    def run(self):
        for _ in range(self.step_limit):
            random_num = random.randint(0, 5)
            if random_num == 0:
                self.x_pos += 1  # Move right
            elif random_num == 1:
                self.x_pos -= 1  # Move left
            elif random_num == 2:
                self.y_pos += 1  # Move forward
            elif random_num == 3:
                self.y_pos -= 1  # Move backward
            elif random_num == 4:
                self.z_pos += 1  # Move up
            else:
                self.z_pos -= 1  # Move down
            self.history.append((self.x_pos, self.y_pos, self.z_pos))
        return (self.x_pos, self.y_pos, self.z_pos)
    
    def plot(self):
        x_vals = [pos[0] for pos in self.history]
        y_vals = [pos[1] for pos in self.history]
        z_vals = [pos[2] for pos in self.history]

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(x_vals, y_vals, z_vals, marker='o')
        ax.set_title('3D Random Walk Path')
        ax.set_xlabel('X Position')
        ax.set_ylabel('Y Position')
        ax.set_zlabel('Z Position')
        plt.show()

    def multi_run(self, runs=10):
        results = []
        for _ in range(runs):
            result = self.run()
            results.append(result)
            self.x_pos = 0
            self.y_pos = 0
            self.z_pos = 0
            self.history = [(self.x_pos, self.y_pos, self.z_pos)]

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter([res[0] for res in results], [res[1] for res in results], [res[2] for res in results], c='r', alpha=0.5)
        ax.set_title('3D Random Walk End Positions')
        ax.set_xlabel('X Position')
        ax.set_ylabel('Y Position')
        ax.set_zlabel('Z Position')
        ax.set_xlim(-self.step_limit, self.step_limit)
        ax.set_ylim(-self.step_limit, self.step_limit)
        ax.set_zlim(-self.step_limit, self.step_limit)
        plt.show()

if __name__ == "__main__":
    walk_3d = RandomWalk3D(step_limit=100)
    walk_3d.multi_run(100)
