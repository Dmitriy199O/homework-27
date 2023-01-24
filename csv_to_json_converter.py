import json
import csv


def csv_to_json(csv_file: str, json_file: str) -> None:
    json_array = []
    with open(csv_file, 'r', encoding='utf8') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            json_array.append(row)

    with open(json_file, 'w', encoding='utf-8') as json_f:
        json_string = json.dumps(json_array,ensure_ascii=False, indent=2)
        json_f.write(json_string)


csv_to_json(csv_file='datasets/ads.csv', json_file='ads/fixtures/ads.json')
csv_to_json(csv_file='datasets/categories.csv', json_file='ads/fixtures/categories.json')
