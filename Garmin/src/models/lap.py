#!/usr/bin/env python3

from formatter import Formatter
from models.swim_stroke import SwimStroke

class Lap:
    @classmethod
    def is_rest(cls, dict):
        return dict["distance"] <= 0 # Assume 0 distance is a rest lap
        
    def __init__(self, dict):
        self.distance_m = dict["distance"]
        self.duration_s = dict["movingDuration"]
        self.formatter = Formatter(self.distance_m, self.duration_s)
        self.strokes = SwimStroke.comma_separated(dict)
        
    def description(self):
        formatted_distance = self.formatter.distance_meters()
        formatted_pace = self.formatter.minutes_per_hundred_meters()
        strokes = self.strokes
        if strokes: strokes = f" ({strokes})"
        return f"{formatted_distance} {formatted_pace}{strokes}"
    
    def process(self):
        print(self.description())