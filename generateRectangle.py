import csv
import random

num_rectangles = 1000

def generate_rectangle():
    x = random.uniform(0, 100)
    y = random.uniform(0, 100)
    width = random.uniform(10, 30)
    height = random.uniform(10, 30)
    A = (x, y)
    B = (x, y + height)
    C = (x + width, y + height)
    D = (x + width, y)
    return A, B, C, D

csv_filename = 'retangulos.csv'

with open(csv_filename, 'w', newline='') as csvfile:
    fieldnames = ['rectangle', 'x_A', 'y_A', 'x_B', 'y_B', 'x_C', 'y_C', 'x_D', 'y_D']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(num_rectangles):
        A, B, C, D = generate_rectangle()
        writer.writerow({
            'rectangle': f'Rectangle {i+1}',
            'x_A': A[0], 'y_A': A[1],
            'x_B': B[0], 'y_B': B[1],
            'x_C': C[0], 'y_C': C[1],
            'x_D': D[0], 'y_D': D[1]
        })
