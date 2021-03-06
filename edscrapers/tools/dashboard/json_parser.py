import os
import sys
import json

from edscrapers.cli import logger

OUTPUT_PATH = os.getenv('ED_OUTPUT_PATH')
try:
    file_path = os.path.join(OUTPUT_PATH, 'statistics.json')
except TypeError:
    logger.error('ED_OUTPUT_PATH env var not set!')
    sys.exit(1)

def read_json_file():

    try:
        with open(file_path) as json_file:
            data = json.load(json_file)
    except:
        logger.error('Cannot read statistics.json file!')

    return data

def get_stats():
    return read_json_file()

def get_total_datasets_number():
    data = read_json_file()
    return data['total']['datopian']['datasets']

def get_total_datasets_data():

    data = read_json_file()

    datasets = data['total']['datopian']['datasets_by_office']

    return datasets

def get_total_pages_data(source):
    data = read_json_file()
    return sum(data['total'][source]['pages'].values())


def get_total_resources_data():

    data = read_json_file()

    datopian_res_number = data['total']['datopian']['resources']
    air_res_number = data['total']['air']['resources']

    return {
        'datopian' : datopian_res_number,
        'air' : air_res_number
    }

def get_total_resources_by_office(source):

    data = read_json_file()
    return data['total'][source]['resources_by_office']

def get_total_pages_by_office(source):

    data = read_json_file()
    return data['total'][source]['pages']

def get_table_rows_by_office(key):
    data = read_json_file()
    scrapers = data['total']['datopian']['datasets_by_office'].keys()
    rows = []
    for s in scrapers:
        rows.append({
            's': s,
            'air': data['total']['air'][key][s],
            'datopian': data['total']['datopian'][key][s]
        })
    return rows

def get_intersection_data():
    data = read_json_file()
    return data['intersections']
