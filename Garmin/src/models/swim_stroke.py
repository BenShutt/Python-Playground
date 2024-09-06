#!/usr/bin/env python3

from enum import Enum

class SwimStroke(Enum):
    BUTTERFLY = 0
    BACKSTROKE = 1
    BREASTSTROKE = 2
    FREESTYLE = 3
    
    def abbreviation(self):
        match self:
            case SwimStroke.BUTTERFLY: return "FL"
            case SwimStroke.BACKSTROKE: return "BK"
            case SwimStroke.BREASTSTROKE: return "BR"
            case SwimStroke.FREESTYLE: return "FR"
    
    @classmethod
    def comma_separated(cls, lap):
        strokes = [] # Ordered list of unique strokes
        
        dtos = lap["lengthDTOs"]
        for dto in dtos:
            key = dto["swimStroke"]
            stroke = SwimStroke[key]
            if stroke != None and stroke not in strokes:
                strokes.append(stroke)

        if len(strokes) == 0:
            return ""
        elif set(strokes) == set(SwimStroke):
            return "IM"
        else:
            return ", ".join([x.abbreviation() for x in strokes])