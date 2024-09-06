#!/usr/bin/env python3

from models.activity import Activity

class Run(Activity):
    """A run activity"""
    
    def __init__(self, dict):
        super().__init__(dict)
        
    def formatted_speed(self):
        """Override, formatting pace in minutes per kilometer (min/km)"""
        return self.formatter.minutes_per_kilometer()