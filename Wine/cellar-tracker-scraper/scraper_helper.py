import csv


def write_to_csv(data, file):
    with open(file, 'a+') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)


def strip_white_space(text):
    """Clean up \n, \xa0 and the likes"""
    to_replace = ['\n', '\xa0', '\t']
    for unwanted in to_replace:
        text = text.replace(unwanted, ' ')  # replace with space
    return text
