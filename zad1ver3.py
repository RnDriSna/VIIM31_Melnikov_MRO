import numpy as np
import matplotlib.pyplot as plt
from math import pi

class Round:
    def __init__(self, x, y, r):
        self.x_batch = []
        self.y_batch = []
        self.x = x
        self.y = y
        self.r = r
        self.batch_size = 20
        self.gen_class()

    def gen_class(self):
        for i in range(self.batch_size):
            self.x_batch.append(np.random.uniform(self.x-self.r, self.x+self.r))
            self.y_batch.append(np.random.uniform(self.y-self.r, self.y+self.r))

    def get_batch_data(self):
        return self.x_batch, self.y_batch

    def get_class_data(self):
        return self.x, self.y, self.r


classes = []
colors = ['yellow', 'orange', 'cyan', 'blue', 'purple', 'red', 'gray']

try:
    with open('input.conf','r') as data:
        counter = 0
        for line in data:
            values=line.split(' ')
            values[len(values)-1]=values[len(values)-1].replace('\n','')
            x, y, r = [float(values[i]) for i in range(len(values))]
            classes.append(Round(x,y,r))
            counter+=1
                 
except FileNotFoundError:
    print('File not found! Manual data input...\n')
    counter = int(input('Class quantity = '))
    for i in range(counter):
        print('Class '.join(str(counter+1)).join('\n'))
        x = float(input('x = '))
        y = float(input('y = '))
        r = float(input('r = '))
        classes.append(Round(x,y,r))


result = open('output.conf', 'w')
t = np.linspace(0, 2*pi, 100)
for i in range(counter):
    x_dat, y_dat = classes[i].get_batch_data()
    x,y,r = classes[i].get_class_data()
    result.write("Class %s\n" % (i+1,))
    result.write("Class Info: %s, %s, %s\n" % (x,y,r))
    for j in range(len(x_dat)):
        result.write("%s, %s; " % (x_dat[j],y_dat[j]))
    result.write('\n')
    plt.scatter(x_dat, y_dat, c=colors[i])
    plt.plot(x+r*np.cos(t), y+r*np.sin(t), color=colors[i])

result.close()

plt.grid(color='lightgray', linestyle='--')
plt.show()
