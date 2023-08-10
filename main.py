import numpy as np
import csv
from utils_functions.write_csv import write_csv
from utils_functions.read_csv import read_csv
from utils_functions.calculate_angle import calculate_angle

def is_reactangle(dots):
   
    list_of_rectangles = []
    margin_percent = 10
    for dot_set in dots:
        pA =[dot_set['x_A'], dot_set['y_A']]
        pB =[dot_set['x_B'], dot_set['y_B']]
        pC =[dot_set['x_C'], dot_set['y_C']]
        pD =[dot_set['x_D'], dot_set['y_D']]
        A = calculate_angle(pD, pA, pB)
        B = calculate_angle(pA, pB, pC)
        C = calculate_angle(pB, pC, pD)
        D = calculate_angle(pC, pD, pA)
        
        if((A + B + C + D) == 360):            
            if(90 - margin_percent <= A <= 90 + margin_percent and 90 - margin_percent <= B <= 90 + margin_percent and 90 - margin_percent <= C <= 90 + margin_percent and 90 - margin_percent <= D <= 90 + margin_percent):
                dot_set['is_retangulo'] = True
                list_of_rectangles.append(dot_set)
        else:
            
            dot_set['retangulo'] = False
            list_of_rectangles.append(dot_set)
            
    return list_of_rectangles
    

def main():
        
    dots = read_csv('casos.csv')
    data_with_margin = is_reactangle(dots)
    write_csv(data_with_margin)

main()