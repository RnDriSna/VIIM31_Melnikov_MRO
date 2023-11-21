import numpy as np

# Примеры точек
point1 = np.array([1, 2, 3])
point2 = np.array([4, 5, 6])

# Евклидово расстояние
euclidean= np.sqrt(np.sum((point1 - point2)**2))
print("Евклидово расстояние:", euclidean)

# Манхэттенское расстояние
manhattan = np.sum(np.abs(point1 - point2))
print("Манхэттенское расстояние:", manhattan)

# Расстояние Минковского
p = 3  # Параметр, определяющий порядок расстояния Минковского
minkowski = np.power(np.sum(np.power(np.abs(point1 - point2), p)), 1/p)
print("Расстояние Минковского:", minkowski)

# Расстояние Канберры
canberra = np.sum(np.abs(point1 - point2) / (np.abs(point1) + np.abs(point2)))
print("Расстояние Канберры:", canberra)