#!/usr/bin/python3
"""
Adds all arguments to a Python list and saves them to a file.
"""
import sys
import os.path

# Importing functions from previous tasks
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# 1. Load existing items if the file exists
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# 2. Add new arguments (excluding the script name itself)
# sys.argv[1:] captures everything after "./7-add_item.py"
items.extend(sys.argv[1:])

# 3. Save the updated list back to the file
save_to_json_file(items, filename)
