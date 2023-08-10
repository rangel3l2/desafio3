import csv
import random

num_cases = 1000  # Número total de casos

def generate_rectangle():
    x = random.uniform(0, 100)
    y = random.uniform(0, 100)
    width = random.uniform(10, 30)
    height = random.uniform(10, 30)
    A = (x, y)
    B = (x + width, y)
    C = (x + width, y + height)
    D = (x, y + height)
    return A, B, C, D

def generate_non_rectangle():
    points = []
    for _ in range(4):
        x = random.uniform(0, 100)
        y = random.uniform(0, 100)
        points.append((x, y))
    return points

csv_filename = 'casos.csv'

with open(csv_filename, 'w', newline='') as csvfile:
    fieldnames = ['retangulo', 'x_A', 'y_A', 'x_B', 'y_B', 'x_C', 'y_C', 'x_D', 'y_D']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(num_cases):
        is_rectangle = random.choice([True, False])
        if is_rectangle:
            A, B, C, D = generate_rectangle()
            retangulo = 'True'
        else:
            points = generate_non_rectangle()
            A, B, C, D = points[0], points[1], points[2], points[3]
            retangulo = 'False'
        
        writer.writerow({
            'retangulo': retangulo,
            'x_A': A[0], 'y_A': A[1],
            'x_B': B[0], 'y_B': B[1],
            'x_C': C[0], 'y_C': C[1],
            'x_D': D[0], 'y_D': D[1]
        })
