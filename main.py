import csv
import json
import uuid
from zipfile import ZipFile


def convert_json(csvFilePath, jsonFilePath):
    data = []

    with open(csvFilePath, encoding='windows-1250') as csvf:
        csvReader = csv.DictReader(csvf, dialect='excel', delimiter=';')

        for rows in csvReader:
            rows['id'] = str(uuid.uuid4())
            data.append(rows)

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=2))


def create_manifest(jsonFilePath_2, author):
    manifest = {
        "id": str(uuid.uuid4()),
        "description": "",
        "author": author,
        "last_update": "2021-11-29T14:03:35Z",
        "type": "ISSUES_TEMPLATES",
        "version": "1.0.0",
        "format": 1,
        "locale": "unk",
        "name": "import_me"
    }
    with open(jsonFilePath_2, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(manifest, indent=2))


csvFilePath = r'talalatsablon.csv'
jsonFilePath = r'data.json'
jsonFilePath_2 = r'manifest.json'
convert_json(csvFilePath, jsonFilePath)
author = 'mildiko'
create_manifest(jsonFilePath_2, author)
zipObj = ZipFile('import_me.zip', 'w')
zipObj.write('data.json')
zipObj.write('manifest.json')
zipObj.close()