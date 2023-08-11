from utils_functions.write_csv import write_csv
from utils_functions.read_csv import *
from utils_functions.calculate_angle import calculate_angle

def is_rectangle(dots):
   
    list_of_rectangles = []
    margin_percent = 30
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
            # print(f"{item['number_rectangle']} is rectangle")
            is_rect += 1 
        else: 
            # print(f"{item['number_rectangle']} is not rectangle")            
            non_react += 1

    print(f'Quantidade de retangulos verdadeiros com margem: {is_rect}')
    # print(f'Quantidade de retangulos falsos: {non_react}')

    acertos = (is_rect/len(data)) * 100    
    return acertos
        

def main():
    dots = read_csv('casos.csv')
    
    lines = count_csv_lines('casos.csv')
    amount_of_hits = cont_csv_condition('casos.csv')
    print(f'Quantidade de retangulos do arquivo de base: {amount_of_hits}')
    percent = (amount_of_hits/lines) * 100

    data_with_margin = is_rectangle(dots)
    write_csv(data_with_margin)
    acertos = resulteds(data_with_margin)

    print(f'banco = {percent:.2f}% com margem = {acertos:.2f}% diferença de {abs(acertos - percent):.2f}%')


main()