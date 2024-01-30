import json
import sys
import argparse

import requests
from prettytable import PrettyTable


BASE_URL = "https://restcountries.com/v2"


def get_country_information(country_name):
    try:
        response = requests.get(f"{BASE_URL}/name/{country_name}")
        if response.status_code != 200:
            raise Exception("Not found")
        parse_json_infos(json.loads(response.content)[0])
    except:
        print("Data not found")


def parse_json_infos(data=None):
    if data != None:
        print("##########################################")
        table = PrettyTable()
        table.field_names = ["Name", "Data"]
        table.add_row(["Country", data['name']])
        table.add_row(["Capital", data['capital']])
        table.add_row(["Population", data['population']])
        table.add_row(["Region", data['region']])
        table.add_row(["Currency Name", data['currencies'][0]['name']])
        table.add_row(["Currency Symbol", data['currencies'][0]['symbol']])
        table.align = "l"
        print(table)
        print("#########################################")



if __name__ == "__main__":
    print("## Welcome to the world of countries! ##")
    print("Usage: python3 main.py <country_name>")
    parser = argparse.ArgumentParser(description='Process informations')
    parser.add_argument('country', type=str, help='Country name to search.')
    args = parser.parse_args()
    get_country_information(args.country)
    print("Byee!")


