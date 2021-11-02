"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    # Set up field name list and empty data list.
    fieldnames = ['datetime_utc', 'distance_au', 'velocity_km_s', 'designation',
                  'name', 'diameter_km', 'potentially_hazardous']
    data = []
    # Write the results to a CSV file, following the specification in the instructions.
    for obj in results:
        # Check for name if no name then name is empty string
        if obj.neo.name:
            name = obj.neo.name
        else:
            name = r''

        # Append data list with dictionary of data per obj
        data.append({'datetime_utc': obj.time_str, 'distance_au': obj.distance,
                     'velocity_km_s': obj.velocity, 'designation': obj.neo.designation,
                     'name': name, 'diameter_km': obj.neo.diameter,
                     'potentially_hazardous': str(obj.neo.hazardous)})

    # Write out a csv file with the given filename
    with open(filename, 'w', newline="") as csvfile:
        # creating a csv writer object
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # writing the header
        writer.writeheader()

        # writing the data rows
        for d in data:
            writer.writerow(d)


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    # Create an empty data list to populate with results
    data = []
    # Write the results to a JSON file, following the specification in the instructions.
    for obj in results:
        # Build out the neo data dict
        neo = {"designation": obj.neo.designation,
               "name": obj.neo.name,
               "diameter_km": obj.neo.diameter,
               "potentially_hazardous": obj.neo.hazardous}

        # Build out the close approach object dict that includes the neo dict from above
        close_obj = {'datetime_utc': obj.time_str,
                     'distance_au': obj.distance,
                     'velocity_km_s': obj.velocity,
                     'neo': neo}
        data.append(close_obj)

    # Write out json file with data
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
