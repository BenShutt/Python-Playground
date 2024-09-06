#!/usr/bin/env python3

"""
Fetch and log Garmin activities.
"""

import sys
import os
import datetime
import argparse
import json

from garmin_api import init_api
from activity_type import ActivityType

# Number of days before now to fetch activities
ACTIVITIES_IN_LAST_DAYS = 3

# ==================== Functions ====================

def init_arguments():
    file_name = os.path.basename(sys.argv[0])
    parser = argparse.ArgumentParser(file_name)
    parser.add_argument("-u", "--username", help="Garmin Connect username", type=str, required=True)
    parser.add_argument("-p", "--password", help="Garmin Connect password", type=str, required=True)
    parser.add_argument("-t", "--tokens", help="Directory to write OAuth tokens", type=str, required=True)
    return parser.parse_args()

def fetch_activities(api):
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(ACTIVITIES_IN_LAST_DAYS)
    return api.get_activities_by_date(start_date.isoformat(), end_date.isoformat())

def print_json(dict):
    print(json.dumps(dict, indent=4))

# ==================== Main ====================

if __name__ == "__main__":
    args = init_arguments()
    api = init_api(args)
    activities = fetch_activities(api)
    for activity in activities:
        model = ActivityType.activity(activity)
        if model != None:
            model.process(api)