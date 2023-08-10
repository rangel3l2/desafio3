import csv
csv_filename = 'casoswithmargin.csv'

def write_csv(data_with_margin):
    for index, data in enumerate(data_with_margin, start=1):
        data['number_rectangle'] = f'Retângulo {index}'
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['number_rectangle', 'x_A', 'y_A', 'x_B', 'y_B', 'x_C', 'y_C', 'x_D', 'y_D', 'is_retangulo', 'retangulo']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for data in data_with_margin:
            writer.writerow(data)