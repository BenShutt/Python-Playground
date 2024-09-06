#!/usr/bin/env python3

import datetime
from pathlib import Path
from formatter import Formatter

# Garmin GMT date format
GARMIN_GMT_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# Date format to print
DATE_FORMAT = "%A %d of %B %Y (%H:%M)"

class Activity:
    """Parent class for Garmin activity models"""

    def __init__(self, dict):
        self.id = dict["activityId"]
        self.start_time_gmt = dict["startTimeGMT"] # String
        self.distance_m = dict["distance"] # Double
        self.duration_s = dict["movingDuration"] # Double
        self.formatter = Formatter(self.distance_m, self.duration_s)
        
    # ==================== Formatting ====================

    def formatted_date_time(self):
        """Map a formatted Garmin date string to a localized formatted date string"""

        # Get the user's time zone
        local_time_zone_id = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo 

        # Get the UTC time zone
        utc_time_zone_id = datetime.timezone.utc

        # Parse the GMT formatted date string
        instant = datetime.datetime.strptime(self.start_time_gmt, GARMIN_GMT_DATE_FORMAT)
        instant = instant.replace(tzinfo=utc_time_zone_id)
    
        # Format in local time
        instant = instant.astimezone(local_time_zone_id)
        return instant.strftime(DATE_FORMAT)
    
    def formatted_type(self):
        """Defaults to the class name"""
        return self.__class__.__name__
    
    def formatted_duration(self):
        """Defaults to duration in hour, minutes, seconds (HH:MM:SS)"""
        return self.formatter.duration()
    
    def formatted_distance(self):
        """Defaults to distance in kilometers (km)"""
        return self.formatter.distance_kilometers()
    
    def formatted_speed(self):
        """Defaults to speed in kilometers per hour (km/h)"""
        return self.formatter.kilometers_per_hour()
    
    # ==================== Other ====================
    
    def download_tcx(self, api):
        data = api.download_activity(self.id, dl_fmt=api.ActivityDownloadFormat.TCX)
        file = f"{str(Path.home())}/Downloads/{self.id}.tcx"
        with open(file, "wb") as writer:
            writer.write(data)
        print(f"TCX written to {file}")
    
    def description(self):
        return (
            f"{self.formatted_date_time()}"
            f", {self.formatted_type()}"
            f", {self.formatted_duration()}"
            f", {self.formatted_distance()}"
            f", {self.formatted_speed()}"
        )  

    def process(self, api, args):
        print(self.description())
