#!/usr/bin/env python3

"""
Fetch and log Garmin activities.
"""

import sys
import os
import argparse
import datetime

from garminconnect import Garmin

# Number of since now to fetch activities
DAYS_AGO = 3

# User must provide a username and password for authentication as
# command-line arguments.
file_name = os.path.basename(sys.argv[0])
parser = argparse.ArgumentParser(file_name)
parser.add_argument("-u", "--username", help="Your Garmin Connect username", type=str, required=True)
parser.add_argument("-p", "--password", help="Your Garmin Connect password", type=str, required=True)
args = parser.parse_args()

# Log in to the Garmin Connect API
api = Garmin(args.username, args.password)
api.login()

# Get the date to fetch activities since
end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(DAYS_AGO)

# Fetch activities
activities = api.get_activities_by_date(start_date.isoformat(), end_date.isoformat())

# Download activities
for activity in activities:
    activity_id = activity["activityId"]
    activity_name = activity["activityName"]
    activity_type = activity["activityType"]["typeKey"]
    activity_date_string = activity["startTimeGMT"]
    activity_date = datetime.datetime.strptime(activity_date_string, "%Y-%m-%d %H:%M:%S")
    print(f"activity_id={activity_id}, activity_name={activity_name}, activity_type={activity_type}, activity_date={activity_date}")
