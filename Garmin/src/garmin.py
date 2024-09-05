#!/usr/bin/env python3

"""
Fetch and log Garmin activities.
"""

import sys
import os
import datetime
import argparse

from activity_type import Activity_Type
from activity import Activity
from run import Run
from ride import Ride
from swim import Swim

from garminconnect import Garmin

# Number of days before now to fetch activities
ACTIVITIES_IN_LAST_DAYS = 3

# ==================== Functions ====================

def parse_arguments():
    # Require username and password for authentication as command-line arguments.
    file_name = os.path.basename(sys.argv[0])
    parser = argparse.ArgumentParser(file_name)
    parser.add_argument("-u", "--username", help="Your Garmin Connect username", type=str, required=True)
    parser.add_argument("-p", "--password", help="Your Garmin Connect password", type=str, required=True)
    return parser.parse_args()

def fetch_activities(args):
    # Log in to the Garmin Connect API
    api = Garmin(args.username, args.password)
    api.login()

    # Get the date to fetch activities since
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(ACTIVITIES_IN_LAST_DAYS)

    # Fetch activities
    return api.get_activities_by_date(start_date.isoformat(), end_date.isoformat())

def init_activity(activity):
    activity_type = Activity_Type.init(activity)
    if activity_type == Activity_Type.RUN:
        return Run(activity)
    elif activity_type == Activity_Type.RIDE:
        return Ride(activity)
    elif activity_type == Activity_Type.SWIM:
        return Swim(activity)

# ==================== Main ====================

if __name__ == "__main__":
    args = parse_arguments()
    activities = fetch_activities(args)
    for activity in activities:
        model = init_activity(activity)
        if model != None:
            print(model.description())
