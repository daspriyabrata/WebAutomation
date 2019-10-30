import csv

def get_csv_data(csv_path):
    rows = []
    variable_file = open(str(csv_path), "rt")
    data_set = csv.reader(variable_file)
    next(data_set)
    for row in data_set:
        rows.append(row[1:])
    return rows
