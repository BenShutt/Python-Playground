#!/usr/bin/env python3

from enum import Enum 

from run import Run
from ride import Ride
from swim import Swim

class ActivityType(Enum):
    RUN = 0
    RIDE = 1
    SWIM = 2
    
    def title(self):
        self.name.capitalize()
        
    @classmethod
    def init(cls, activity):
        type_key = activity["activityType"]["typeKey"]
        if type_key == "running":
            return cls.RUN
        elif type_key == "cycling":
            return cls.RIDE
        elif type_key == "lap_swimming":
            return cls.SWIM
        else:
            print(f"Unsupported activity_type {type_key}")
            return None
        
    @classmethod
    def activity(cls, activity):
        activity_type = cls.init(activity)
        if activity_type == ActivityType.RUN:
            return Run(activity)
        elif activity_type == ActivityType.RIDE:
            return Ride(activity)
        elif activity_type == ActivityType.SWIM:
            return Swim(activity)
        else:
            return None