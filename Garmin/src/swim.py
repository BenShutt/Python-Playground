#!/usr/bin/env python3

from activity import Activity

class Swim(Activity):
    """A swim activity"""
    
    def __init__(self, dict):
        Activity.__init__(self, dict)