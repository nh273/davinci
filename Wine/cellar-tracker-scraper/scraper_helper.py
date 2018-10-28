import csv
import time
import random


def write_to_csv(fields, dict_data, file):
    with open(file, 'a+') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        for data in dict_data:
            writer.writerow(data)


def strip_white_space(text):
    """Clean up \n, \xa0 and the likes"""
    to_replace = ['\n', '\xa0', '\t']
    for unwanted in to_replace:
        text = text.replace(unwanted, ' ')  # replace with space
    return text


def random_sleep():
    '''Sleep a random amount of time'''
    timeout = random.randint(5, 12)
    timeout += random.randint(0, 100)/100
    time.sleep(timeout)
