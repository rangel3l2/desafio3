import numpy as np

def calculate_angle(p1, encontro, p2):  
    vet1 = np.array(p1) - np.array(encontro)
    vet2 = np.array(p2) - np.array(encontro)
    cos = np.dot(vet1, vet2) / (np.linalg.norm(vet1) * np.linalg.norm(vet2))   
    rad = np.arccos(cos)  
    deg = np.degrees(rad)
    return deg


def is_rectangle(dots, margin):
    list_of_rectangles = []
    margin_percent = margin

    for dot_set in dots:
        pA =[dot_set['x_A'], dot_set['y_A']]
        pB =[dot_set['x_B'], dot_set['y_B']]
        pC =[dot_set['x_C'], dot_set['y_C']]
        pD =[dot_set['x_D'], dot_set['y_D']]
        A = max(calculate_angle(pD, pA, pB), calculate_angle(pC, pA, pB), calculate_angle(pD, pA, pC))
        B = max(calculate_angle(pA, pB, pC), calculate_angle(pD, pB, pC), calculate_angle(pA, pB, pD))
        C = max(calculate_angle(pB, pC, pD), calculate_angle(pA, pC, pD), calculate_angle(pB, pC, pA))
        D = max(calculate_angle(pC, pD, pA), calculate_angle(pB, pD, pA), calculate_angle(pC, pD, pB))
        
        if((A + B + C + D) == 360):      
            if(90 - margin_percent <= A <= 90 + margin_percent and 90 - margin_percent <= B <= 90 + margin_percent and 90 - margin_percent <= C <= 90 + margin_percent and 90 - margin_percent <= D <= 90 + margin_percent):
                dot_set['is_rectangle'] = True
                list_of_rectangles.append(dot_set)
            else:
                dot_set['is_rectangle'] = False
                list_of_rectangles.append(dot_set)
        else:
            dot_set['is_rectangle'] = False
            list_of_rectangles.append(dot_set)

    for index, data in enumerate(list_of_rectangles):
        data['number_rectangle'] = f'Retângulo {index}'
            
    return list_of_rectangles


def resulteds(data):
    is_rect = 0
    non_react = 0
    
    for item in data:
        if item['is_rectangle'] == True:
            is_rect += 1 
        else: 
            non_react += 1
    
    return is_rect