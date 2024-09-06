#!/usr/bin/env python3

from activity import Activity

class Run(Activity):
    """A run activity"""
    
    def __init__(self, dict):
        super().__init__(dict)
        