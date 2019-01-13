import json, os


def percentage_of_words(json_file_name, string_string):
    with open(os.path.join(os.path.dirname(__file__), '..', 'data', json_file_name + '.json')) as f:
        data = json.load(f)
    counter = 0
    for i in data[json_file_name]:
        counter += string_string.count(i)
    return counter/string_string.count(" ")
