import numpy as np
import csv

def is_geometry(dots):
    list_dot = []
    for dot in dots:
        list_dot.append(float(dot))
        
        
    
    AB = abs(np.sqrt(np.power(list_dot[1][0] - list_dot[0][0], 2) + np.power(list_dot[1][1] - list_dot[0][1], 2)))
   
    BC =abs(np.sqrt(np.power(list_dot[2][0] - list_dot[1][0], 2) + np.power(list_dot[2][1] - list_dot[1][1], 2)))
    
    CD = abs(np.sqrt(np.power(list_dot[3][0] - list_dot[2][0], 2) + np.power(list_dot[3][1] - list_dot[2][1], 2)))
                        
    DA = abs(np.sqrt(np.power(list_dot[0][0] - list_dot[3][0], 2) + np.power(list_dot[0][1] - list_dot[3][1], 2)))

    if(AB == BC == CD == DA):
        return 'retangulo'
    
    if(AB == CD and BC == DA):
        return 'retangulo'
    
    return 'nao é'
        


def read_csv(csv_file):
    pontos = []
    with open(csv_file, 'r') as csv_file:
        
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:            
            pontos.append(line)
    return pontos

def main():
     data = read_csv('retangulos.csv')
     is_geometry(data)
     
    
main()