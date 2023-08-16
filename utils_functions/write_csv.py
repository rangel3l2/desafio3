import csv

csv_filename = 'casoswithmargin.csv'

def write_csv(data_with_margin):
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['number_rectangle', 'x_A', 'y_A', 'x_B', 'y_B', 'x_C', 'y_C', 'x_D', 'y_D', 'is_rectangle']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for data in data_with_margin:
            writer.writerow(data)