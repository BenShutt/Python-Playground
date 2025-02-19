#!/usr/bin/env python3

from models.activity import Activity
from models.lap import Lap

class Swim(Activity):
    """A swim activity"""
    
    def __init__(self, dict):
        super().__init__(dict)
        
    def formatted_distance(self):
        """Override, formatting distance in meters (m)"""
        return self.formatter.distance_meters()
        
    def formatted_speed(self):
        """Override, formatting pace in minutes per hundred meters (min/100m)"""
        return self.formatter.minutes_per_hundred_meters()

    def process(self, api, args):
        super().process(api, args)

        if not args.laps: return
        splits = api.get_activity_splits(self.id)
        laps = splits["lapDTOs"]
        for dict in laps:
            if not Lap.is_rest(dict):
                Lap(dict).process()
        
            