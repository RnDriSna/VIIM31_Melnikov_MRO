import numpy as np
import matplotlib.pyplot as plt

class ImageGenerator:
    def __init__(self, filename):
        self.filename = filename
        self.data = []

    def read_data(self):
        with open(self.filename, 'r') as file:
            lines = file.readlines()
            self.Nk = int(lines[0].strip())
            self.r = int(lines[1].strip())
            self.N = [int(x.strip()) for x in lines[2].split(',')]

    def generate_images(self):
        self.images = []
        for n in self.N:
            images = np.random.uniform(low=0, high=1, size=(n, self.r))
            self.images.append(images)

    def save_images(self):
        with open('images.txt', 'w') as file:
            for i, images in enumerate(self.images):
                file.write(f'Class {i+1}:\n')
                for image in images:
                    file.write(','.join([str(x) for x in image]) + '\n')

    def display_images(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        for i, images in enumerate(self.images):
            ax.scatter(images[:, 0], images[:, 1], images[:, 2], label=f'Class {i+1}')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.legend()
        plt.show()

if __name__ == '__main__':
    generator = ImageGenerator('input.txt')
    generator.read_data()
    generator.generate_images()
    generator.save_images()
    generator.display_images()

