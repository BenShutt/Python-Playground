#!/usr/bin/env python3

import datetime
from pathlib import Path

# Garmin GMT date format
GARMIN_GMT_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# Date format to print
DATE_FORMAT = "%A %d of %B %Y (%H:%M)"

class Activity:
    """Parent class for Garmin activity models"""

    def __init__(self, dict):
        self.id = dict["activityId"]
        self.start_time_gmt = dict["startTimeGMT"] # String
        self.duration_s = dict["movingDuration"] # Double
        self.distance_m = dict["distance"] # Double

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
        return self.__class__.__name__
    
    def formatted_duration(self):
        min, sec = divmod(self.duration_s, 60)
        hour, min = divmod(min, 60)
        return '%02d:%02d:%02d' % (hour, min, sec)
    
    def formatted_distance(self):
        return "{:.2f} km".format(self.distance_m / 1000)
    
    def download_gpx_to_desktop(self, api):
        gpx_data = api.download_activity(self.id, dl_fmt=api.ActivityDownloadFormat.GPX)
        file = f"{str(Path.home())}/Desktop/{self.id}.gpx"
        with open(file, "wb") as writer:
            writer.write(gpx_data)
    
    def description(self):
        return f"{self.formatted_date_time()}, {self.formatted_type()}, {self.formatted_duration()}, {self.formatted_distance()}"
    
    def process(self):
        print(self.description())
