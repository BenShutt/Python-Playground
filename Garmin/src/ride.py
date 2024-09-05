#!/usr/bin/env python3

from activity import Activity

class Ride(Activity):
    """A ride activity"""
    
    def __init__(self, dict):
        Activity.__init__(self, dict)