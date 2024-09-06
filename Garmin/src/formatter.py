#!/usr/bin/env python3

class Formatter:
    def __init__(self, distance_m, duration_s):
        self.distance_m = distance_m
        self.duration_s = duration_s
        
    # ==================== Duration ====================
    
    def duration(self):
        """Formatted duration in hour, minutes, seconds (HH:MM:SS)"""
        minutes, seconds = divmod(self.duration_s, 60)
        hours, minutes = divmod(minutes, 60)
        return "{:02.0f}:{:02.0f}:{:02.0f}".format(hours, minutes, seconds)
        
    # ==================== Distance ====================
        
    def distance_meters(self):
        """Formatted distance in meters (m)"""
        return "{:0.0f}m".format(self.distance_m)
    
    def distance_kilometers(self):
        """Formatted distance in kilometers (km)"""
        distance_km = self.distance_m / 1000
        return "{:.2f}km".format(distance_km)
    
    # ==================== Speed ====================
    
    def kilometers_per_hour(self):
        """Formatted speed in kilometers per hour (km/h)"""
        if self.duration_s <= 0: return "N/A"
        distance_km = self.distance_m / 1000
        duration_h = self.duration_s / 3600
        speed_km_per_h = distance_km / duration_h
        return "{:.2f} km/h".format(speed_km_per_h)
    
    # ==================== Pace ====================
    
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
