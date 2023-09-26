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
            if self.r == 2:
                images = np.random.rand(n, self.r)
            else:
                images = np.random.rand(self.r, n)
            self.images.append(images)

    def save_images(self):
        with open('images.txt', 'w') as file:
            for i, images in enumerate(self.images):
                file.write(f'Class {i+1}:\n')
                for image in images:
                    file.write(','.join([str(x) for x in image]) + '\n')

    def display_images(self):
        fig, axs = plt.subplots(self.Nk, self.r)
        fig.suptitle('Image Visualization')
        for i in range(self.Nk):
            for j in range(self.r):
                axs[i, j].imshow(self.images[i][:,j].reshape((self.N[i], 1)))
                axs[i, j].axis('off')
        plt.show()

if __name__ == '__main__':
    generator = ImageGenerator('input.txt')
    generator.read_data()
    generator.generate_images()
    generator.save_images()
    generator.display_images()

