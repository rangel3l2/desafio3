import csv

def read_csv(csv_file):
    dots = []
    with open(csv_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        headers = next(csv_reader) 
        
        for line in csv_reader:
            dot_dict = {}
            for i, header in enumerate(headers):           
                if header != 'rectangle' and header != 'is_rectangle':
                    dot_dict[header] = float(line[i])
            dots.append(dot_dict)
            
    return dots


def count_csv_lines(csv_file):
    with open(csv_file, mode="r") as file:
        reader = csv.reader(file)
        num_lines = sum(1 for _ in reader)

    return num_lines - 1


def cont_csv_condition(csv_file):
    cont = 0
    with open(csv_file, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == 'True':
                cont += 1
    
    return cont