import csv


def write_to_csv(data, file):
    with open(file, 'a+') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)
