import numpy as np
import csv

def is_geometry(dots):
    
  
    rectangle_count = 0
    non_rectangle_count = 0
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
            print(f'A{A} + B{B} + C{C} + D{D}')
            if(90 - margin_percent <= A <= 90 + margin_percent and 90 - margin_percent <= B <= 90 + margin_percent and 90 - margin_percent <= C <= 90 + margin_percent and 90 - margin_percent <= D <= 90 + margin_percent):
                print(f'entrou na margem = A{A} + B{B} + C{C} + D{D}')
                rectangle_count += 1
    
def calculate_angle(p1, encontro, p2):
    #ponto medio em relacao ao ponto (0,0)
    #facilidade para realização dos cálculos
    vet1 = np.array(p1) - np.array(encontro)
    vet2 = np.array(p2) - np.array(encontro)

    #formula usada para encontrar o cosseno do angulo entre os vetores
    #divisão do produto escalar pela multiplicação das magnitudes dos vetores
    #a magnitude nesse contexto está retornando a distancia entre os pontos
    cos = np.dot(vet1, vet2) / (np.linalg.norm(vet1) * np.linalg.norm(vet2))
    
    #calcula em radianos o cosseno encontrado
    rad = np.arccos(cos)
    #converte o angulo em radianos para graus
    deg = np.degrees(rad)
    return deg
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