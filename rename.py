import os
import argparse

class Cfg:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Example script with configurable parameters")

        # Define command-line arguments
        self.parser.add_argument("--path", type=str, help="please input file path")

    def parse_args(self):
        # Parse command-line arguments
        return self.parser.parse_args()
cfg = Cfg()
args = cfg.parse_args()

# Path to the folder containing the PNG or JPG files
folder_path = args.path

# Get a list of all PNG or JPG files in the folder
files = [f for f in os.listdir(folder_path) if f.endswith(".png") or f.endswith(".jpg")]

# Sort the files alphabetically
files.sort()

# Rename and move the files
for i, file in enumerate(files):
    # Generate the new file name
    new_name = "{:04d}.{}".format(i+1, file.split(".")[-1])
    # Rename the file
    os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_name))
    print("Renamed {} to {}".format(file, new_name))

