#!/usr/bin/env python3

"""
Output paces required to achieve target times for each Triathlon discipline.
Times should be formatted as HH:mm.

Example usage:
$ python tri-time.py --swim 00:35 --ride 03:15 --run 01:40
"""

import os
import sys
import datetime
import argparse

class Formatter:
    def __init__(self, distance_m, duration_s):
        self.distance_m = distance_m
        self.duration_s = duration_s
    
    def kilometers_per_hour(self):
        """Formatted speed in kilometers per hour (km/h)"""
        if self.duration_s <= 0: return "N/A"
        distance_km = self.distance_m / 1000
        duration_h = self.duration_s / 3600
        speed_km_per_h = distance_km / duration_h
        return "{:.2f} km/h".format(speed_km_per_h)
    
    def minutes_per_kilometer(self):
        """Formatted pace in minutes per kilometer (min/km)"""
        if self.distance_m <= 0: return "N/A"
        distance_km = self.distance_m / 1000
        pace_s_per_km = self.duration_s / distance_km
        minutes, seconds = divmod(pace_s_per_km, 60)
        return "{:02.0f}:{:02.0f} min/km".format(minutes, seconds)
    
    def minutes_per_hundred_meters(self):
        """Formatted pace in minutes per hundred meters (min/100m)"""        
        if self.distance_m <= 0: return "N/A"
        distance_100m = self.distance_m / 100
        pace_s_per_100m = self.duration_s / distance_100m
        minutes, seconds = divmod(pace_s_per_100m, 60)
        return "{:02.0f}:{:02.0f} min/100m".format(minutes, seconds)

def init_arguments():
    file_name = os.path.basename(sys.argv[0])
    parser = argparse.ArgumentParser(file_name)
    parser.add_argument("--swim", help="Swim duration formatted as HH:mm", type=str, required=True)
    parser.add_argument("--ride", help="Ride duration formatted as HH:mm", type=str, required=True)
    parser.add_argument("--run", help="Run duration formatted as HH:mm", type=str, required=True)
    return parser.parse_args()

def parse_time(time):
    time = datetime.datetime.strptime(time, "%H:%M")
    return 3600 * time.hour + 60 * time.minute

def total_time(swim_s, ride_s, run_s):
    total_s = swim_s + ride_s + run_s
    minutes, _ = divmod(total_s, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02d}:{minutes:02d}"
    
def main():
    args = init_arguments()
    
    swim_distance_m = 1900 # 1.9km
    swim_duration_s = parse_time(args.swim)
    swim_pace = Formatter(swim_distance_m, swim_duration_s).minutes_per_hundred_meters()
    print(f"Swim: {swim_pace}")
    
    ride_distance_m = 90000 # 90km
    ride_duration_s = parse_time(args.ride)
    ride_speed = Formatter(ride_distance_m, ride_duration_s).kilometers_per_hour()
    print(f"Ride: {ride_speed}")
    
    run_distance_m = 21100 # 21.1km
    run_duration_s = parse_time(args.run)
    run_pace = Formatter(run_distance_m, run_duration_s).minutes_per_kilometer()
    print(f"Run: {run_pace}")
    
    total = total_time(swim_duration_s, ride_duration_s, run_duration_s)
    print(f"Total: {total}")
    
if __name__ == "__main__":
    main()