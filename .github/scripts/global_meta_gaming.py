#!/usr/bin/python

import sys
import json
import os.path

def main():
    all_meta_data = []

    src_dir = 'gaming/src'

    for root, dirs, files in os.walk(src_dir):
        dirs.sort(reverse=True)
        files.sort(reverse=True)
        if 'meta.json' in files:
            meta_file_path = os.path.join(root, 'meta.json')
            with open(meta_file_path, 'r') as meta_file:
                modified_meta_json = json.loads(meta_file.read())
                modified_meta_json['uri'] = meta_file_path.replace("gaming/src/", "").replace("/meta.json", "")
                found = False
                for i in all_meta_data:
                    if i['uri'] == modified_meta_json['uri']:
                        i = modified_meta_json
                        found = True
                        break

                if found == False:
                    if isinstance(modified_meta_json, dict) and modified_meta_json:  # Ensure the content is a non-empty dictionary
                        all_meta_data.append(modified_meta_json)
                    else:
                        print(f"Warning: {meta_file_path} is empty or not a dictionary.")
    sorted_meta_data = sorted(all_meta_data, key=lambda x: x['date'], reverse=True)
    print(json.dumps(sorted_meta_data, sort_keys=True, indent=4, ensure_ascii=False))

main()