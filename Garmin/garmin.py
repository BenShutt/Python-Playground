#!/usr/bin/env python3

"""
Fetch Garmin activities from the last 3 days.
"""

import sys
import os
import argparse
#from garminconnect import Garmin

file_name = os.path.basename(sys.argv[0])
parser = argparse.ArgumentParser(file_name)
parser.add_argument("-u", "--username", help="Your Garmin Connect username", type=str, required=True)
parser.add_argument("-p", "--password", help="Your Garmin Connect password", type=str, required=True)
args = parser.parse_args()

print(args.username)
print(args.password)

#api = Garmin(args.username, args.password)
#api.login()
#print(api.get_full_name())