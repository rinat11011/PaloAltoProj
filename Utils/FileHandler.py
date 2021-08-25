import json
import pandas as pd
import os


def check_files_validity(path):
    return os.path.isfile(path) and os.path.getsize(path) > 0


def open_and_read_file(path):
    # Open and read rules.json file
    with open(path, "r") as rules_f:
        rules_data = rules_f.read()
    return rules_data


def open_file_r(logs_path):
    return open(logs_path, "r")


def create_file_w(out_path):
    return open(out_path, "w")


def append_to_output_file(out, data):
    out.writelines(data)
