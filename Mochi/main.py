#!/usr/bin/env python3

"""
Downloads Mochi images, converts `.webp` to `.png`, and crops.
With thanks to Little Moons.
"""

import requests
import pathlib
import os
import subprocess
import shutil

# User's home directory
HOME = str(pathlib.Path.home())

# Path of the directory to write the images into
DIRECTORY = f"{HOME}/Desktop/MochiImages"

# Mapping of image name to remote URL to download the image from
images = {
    "Caramel": "https://littlemoons.com/wp-content/uploads/2023/09/1_411b0910-1a23-4714-a106-4679cbfd908c.webp",
    "Chocolate": "https://littlemoons.com/wp-content/uploads/2023/09/1_ChocHazelnut.webp",
    "Coconut": "https://littlemoons.com/wp-content/uploads/2023/09/1_coconut.webp",
    "Mango": "https://littlemoons.com/wp-content/uploads/2023/09/1.webp",
    "Pistachio": "https://littlemoons.com/wp-content/uploads/2023/09/1_Pistach.webp",
    "Vanilla": "https://littlemoons.com/wp-content/uploads/2023/09/Vanilla_Packshot_1.png"
}

# Create the directory to download into, deleting existing if necessary 
# (conditional on prompt confirmation).
def init_directory():
    if not os.path.isdir(DIRECTORY):
        pathlib.Path(DIRECTORY).mkdir(parents=True, exist_ok=True)
    else:
        rc = input(f"{DIRECTORY} already exists, delete? ").lower()
        if rc in {"yes", "y"}:
            shutil.rmtree(DIRECTORY)
            init_directory()
        else:
            print("Exiting...")
            exit(0)

# Download the images from the remote into the local directory
def download_images():
    for key, value in images.items():
        extension = pathlib.Path(value).suffix
        file = f"{DIRECTORY}/Mochi{key}{extension}"
        data = requests.get(value).content
        with open(file, "wb") as handler:
            handler.write(data)

# Run a command and raise an exception on non-zero return status
def run_command(command):
    if subprocess.call(command, shell=True) != 0:
        raise SystemExit(f"'{command}' command failed")

# Convert the given entry to a PNG
def convert_to_png(entry):
    from_url = entry.path
    to_url = f"{os.path.splitext(from_url)[0]}.png"
    command = f"magick {from_url} {to_url}"
    run_command(command)
    os.remove(from_url)
    return to_url

# For all PNG and WEBP files, crop the relevant part of the image
def process():
    with os.scandir(DIRECTORY) as it:
        for entry in it:
            path = entry.path
            if entry.is_file() and path.endswith(".webp"):
                path = convert_to_png(entry)
            
            if path.endswith(".png"):
                command = f"magick {path} -crop 540x490+390+550 {path}"
                run_command(command)

# Execute the steps generating the images
def main():
    init_directory()
    download_images()
    process()
    print(f"Images written to '{DIRECTORY}'")

if __name__ == "__main__":
    main()