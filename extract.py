"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach

import logging
logging.basicConfig()

# Create logger and set the log level
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


def load_neos(neo_csv_path=r'C:\Users\alex.jacobs\PycharmProjects\neo\data\neos.csv'):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    logger.debug(f'Loading NEOs from {neo_csv_path}')
    neos = []
    data_dict = {}
    with open(neo_csv_path) as csvfile:
        reader = csv.DictReader(csvfile)
        for data in reader:
            for d, value in data.items():
                data_dict[d] = value
            neos.append(NearEarthObject(data))
    return neos


def load_approaches(cad_json_path=r'C:\Users\alex.jacobs\PycharmProjects\neo\data\cad.json'):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    logger.debug(f'Loading Close Approaches from {cad_json_path}')
    approaches = []
    with open(cad_json_path) as f:
        json_data = json.load(f)
        json_data = [dict(zip(json_data["fields"], data)) for data in json_data["data"]]
    for data in json_data:
        approaches.append((CloseApproach(data)))
    return approaches
