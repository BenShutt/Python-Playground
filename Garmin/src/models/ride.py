#!/usr/bin/env python3

from models.activity import Activity

class Ride(Activity):
    """A ride activity"""
    
    def __init__(self, dict):
        super().__init__(dict)