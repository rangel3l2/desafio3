import csv
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