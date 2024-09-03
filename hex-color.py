"""
Convert #RRGGBB(AA) hex color strings to RGBA format.
Usage: python hex-color.py "#RRGGBBAA"
"""

import sys
import matplotlib.colors
import re

def is_valid_hex_color(hex):
    regex = r"^(([0-9a-fA-F]{2}){3}(?:[0-9a-fA-F]{2})?)$"
    pattern = re.compile(regex)
    return bool(pattern.match(hex))

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc < 2:
        sys.exit("Please provide a #RRGGBBAA hex color command-line argument")
   
    hex = sys.argv[1].strip("#")
    if not is_valid_hex_color(hex):
        sys.exit(f"{hex} is not a valid HEX color")
    
    (r, g, b, a) = matplotlib.colors.to_rgba(f"#{hex}")
    (r255, g255, b255, a255) = (int(r * 255), int(g * 255), int(b * 255), int(a * 255))
    print(f"Range: [0, 1]: {(r, g, b, a)}")
    print(f"Range: [0, 255]: {(r255, g255, b255, a255)}")