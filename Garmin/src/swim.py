#!/usr/bin/env python3

from activity import Activity

class Swim(Activity):
    """A swim activity"""
    
    def __init__(self, dict):
        super().__init__(dict)
        
    def process(self, api):
        super().process(api)
        self.print_laps(api)
        
    def formatted_distance(self):
        return self.formatted_distance_m(self.distance_m)
        
    def formatted_speed(self):
        return self.formatted_pace(self.distance_m, self.duration_s)
        
    def formatted_pace(self, distance_m, duration_s):
        """Formatted pace in minutes / 100meters"""
        number_of_hundreds = distance_m / 100
        seconds_per_hundred = duration_s / number_of_hundreds
        min, sec = divmod(seconds_per_hundred, 60)
        return "%02d:%02d min/100m" % (min, sec)
    
    def formatted_distance_m(self, distance_m):
        """Formatted distance in meters"""
        return "%d m" % distance_m
    
    def print_lap(self, lap):
        distance_m = lap["distance"]
        if distance_m <= 0:
            return # Assume 0 distance is a rest lap
        duration_s = lap["movingDuration"]
        formatted_distance = self.formatted_distance_m(distance_m)
        formatted_pace = self.formatted_pace(distance_m, duration_s)
        print(f"    {formatted_distance} {formatted_pace}")
        
    def print_laps(self, api):
        splits = api.get_activity_splits(self.id)
        laps = splits["lapDTOs"]
        for lap in laps:
            self.print_lap(lap)
            