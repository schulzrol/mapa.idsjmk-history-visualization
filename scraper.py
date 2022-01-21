#!/bin/python3
import os
import requests
import time
from datetime import datetime, timedelta
import argparse

vehicles_api_url = "https://mapa.idsjmk.cz/api/vehicles.json"

default_interval = "0:1:0"
default_runfor = "24:0:0"
default_folder = "./output/"

def main():
    start_time = datetime.now()

    parser = argparse.ArgumentParser(description='Scrape vehicle data from idsjmk')
    parser.add_argument('--output-folder', help='output folder', default=default_folder, type=str, nargs='?')
    parser.add_argument('--every', type=str, nargs='?', help='scrape every time interval', default=default_interval)
    parser.add_argument('--run-for', help='run for how much long', default=default_runfor, nargs='?', type=str)

    args = parser.parse_args()
    hours, mins, secs = tuple(map(int, args.run_for.split(":")))
    end_time = start_time + timedelta(hours=hours, minutes=mins, seconds=secs)

    hours, mins, secs = tuple(map(int, args.every.split(":")))
    seconds_every = hours*(60*60) + mins*60 + secs
    os.makedirs(args.output_folder, exist_ok=True)

    # loop
    while (datetime.now() <= end_time):
        filename = datetime.now().strftime("%Y.%m.%d %H:%M:%S") + ".json"
        # scrape
        raw_vehicles_json = requests.get(vehicles_api_url)

        # save
        filepath = os.path.join(args.output_folder, filename)
        with open(filepath, "wb") as f:
            f.write(raw_vehicles_json.content)

        # sleep interval
        time.sleep(seconds_every)


    

if __name__ == "__main__":
    main()