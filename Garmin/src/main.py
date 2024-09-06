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

from models.activity_type import ActivityType

# ==================== Functions ====================

def init_arguments():
    file_name = os.path.basename(sys.argv[0])
    parser = argparse.ArgumentParser(file_name)
    parser.add_argument("--tokens", help="Directory to store OAuth tokens", type=str, required=True)
    parser.add_argument("--json", action="store_true", help="Print activities as JSON")
    parser.add_argument("--days", help="Days before now to fetch activities", type=int, required=True)
    parser.add_argument("--laps", action="store_true", help="Show splits for swimming activities")
    return parser.parse_args()

def fetch_activities(args, api):
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(args.days)
    return api.get_activities_by_date(start_date.isoformat(), end_date.isoformat())

def print_json(dict):
    print(json.dumps(dict, indent=4))

# ==================== Main ====================

if __name__ == "__main__":
    args = init_arguments()
    api = init_api(args)
    activities = fetch_activities(args, api)
    for activity in activities:
        if args.json:
            print_json(activity)

        model = ActivityType.activity(activity)
        if model != None:
            model.process(api, args)