import numpy as np
import csv

def is_geometry(dots):
    rectangle_count = 0
    non_rectangle_count = 0
    
    for dot_set in dots:
        AB = abs(np.sqrt(np.power(dot_set['x_B'] - dot_set['x_A'], 2) + np.power(dot_set['y_B'] - dot_set['y_A'], 2)))
        BC = abs(np.sqrt(np.power(dot_set['x_C'] - dot_set['x_B'], 2) + np.power(dot_set['y_C'] - dot_set['y_B'], 2)))
        CD = abs(np.sqrt(np.power(dot_set['x_D'] - dot_set['x_C'], 2) + np.power(dot_set['y_D'] - dot_set['y_C'], 2)))
        DA = abs(np.sqrt(np.power(dot_set['x_A'] - dot_set['x_D'], 2) + np.power(dot_set['y_A'] - dot_set['y_D'], 2)))

        if (AB == BC == CD == DA) or (AB == CD and BC == DA):
            rectangle_count += 1
        else:
            non_rectangle_count += 1    
    return rectangle_count, non_rectangle_count

def read_csv(csv_file):
    dots = []
    with open(csv_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        headers = next(csv_reader) 
        
        for line in csv_reader:
            dot_dict = {}
            for i, header in enumerate(headers):                  
                if header != 'retangulo' and header != 'is_retangulo':
                    dot_dict[header] = float(line[i])
            dots.append(dot_dict)
            
    return dots
def main():
        
        dots = read_csv('casos.csv')
        rectangle, non_rectangle = is_geometry(dots)
        print(f'Quantity of rectangles:{rectangle}')
        print(f'Quantity of non-rectangles:{non_rectangle}')
    

main()