import json
import os

import requests

filename = 'task_kmr/docs.json'

with open(filename) as f:
    file = json.load(f)

for document in file:
    content = requests.get(document['link']).content
    f_name = f"{document['name'].replace(' ', '_')}.txt"
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dest_dir = os.path.join(script_dir, 'kmr_documents')
    try:
        os.makedirs(dest_dir)
    except OSError:
        pass
    path = os.path.join(dest_dir, f_name)
    with open(path, 'wb') as file:
        file.write(content)
