#!/usr/bin/env python3

from formatter import Formatter

class Lap:
    @classmethod
    def is_rest(cls, dict):
        return dict["distance"] <= 0 # Assume 0 distance is a rest lap
        
    def __init__(self, dict):
        self.distance_m = dict["distance"]
        self.duration_s = dict["movingDuration"]
        self.formatter = Formatter(self.distance_m, self.duration_s)
        
    def description(self):
        formatted_distance = self.formatter.distance_meters()
        formatted_pace = self.formatter.minutes_per_hundred_meters()
        return f"{formatted_distance} @ {formatted_pace}"
    
    def process(self):
        print(f"    {self.description()}")