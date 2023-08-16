from utils_functions.write_csv import write_csv
from utils_functions.read_csv import *
from utils_functions.calculate_angle import *

def main():
    num_data = count_csv_lines('casos.csv')
    rect_data = cont_csv_condition('casos.csv')

    margem = float(input("Qual a margem de erro do angulo do retangulo: " ))

    print(f'Quantidade de retangulos do arquivo de geração: {rect_data}')
    percent_generate = (rect_data/num_data) * 100

    dots = read_csv('casos.csv')
    data_with_margin = is_rectangle(dots, margem)
    rect_with_margin = resulteds(data_with_margin)
    
    write_csv(data_with_margin)

    percent_with_margin = (rect_with_margin/len(dots)) * 100

    print(f'retangulos gerados = {percent_generate:.2f}%')
    print(f'retangulos com margem = {percent_with_margin:.2f}%') 
    print(f'diferença de acertos: {abs(percent_with_margin - percent_generate):.2f}%')

main()