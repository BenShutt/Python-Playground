#!/usr/bin/env python3

from activity import Activity

class Run(Activity):
    """A run activity"""
    
    def __init__(self, dict):
        super().__init__(dict)
        
    def formatted_speed(self):
        """For running, show pace in minutes / kilometer"""
        if self.distance_m <= 0: return "N/A"
        distance_km = self.distance_m / 1000
        seconds_per_km = self.duration_s / distance_km
        minutes, seconds = divmod(seconds_per_km, 60)
        return "{:02.0f}:{:02.0f} min/km".format(minutes, seconds)