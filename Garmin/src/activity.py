#!/usr/bin/env python3

import datetime

# Garmin GMT date format
GARMIN_GMT_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# Date format to print
DATE_FORMAT = "%A %d of %B %Y (%H:%M)"

class Activity:
    """Parent class for Garmin activity models"""

    def __init__(self, dict):
        self.start_time_gmt = dict["startTimeGMT"] # String
        self.duration = dict["duration"] # Double

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
        return "{:0>8}".format(str(datetime.timedelta(seconds=self.duration)))
    
    def description(self):
        return f"{self.formatted_date_time()}, {self.formatted_type()}, {self.formatted_duration()}"
