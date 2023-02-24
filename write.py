import csv
import json


def write_csv(note_data):
    with open('database.csv', 'w', encoding="utf-8") as file:
        writer = csv.writer(file)
        for note in note_data:
            writer.writerow(note.values())

def write_json(note_data):
    with open('database02.json', 'w') as outfile:
        json.dump(note_data, outfile)