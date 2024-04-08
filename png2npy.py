import argparse
import numpy as np
import os

class Cfg:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Convert PNG files in a folder to a single .npy file")
        # Define command-line arguments
        self.parser.add_argument("--input_path", type=str, required=True, help="Path to the input folder containing PNG files")
        self.parser.add_argument("--output_path", type=str, required=True, help="Path to the output .npy file")
    def parse_args(self):
        # Parse command-line arguments
        return self.parser.parse_args()

import numpy as np
import os
from PIL import Image

def convert_png_to_npy(input_folder, output_file, target_size=(1024,1024)):
    # Get list of PNG or JPG files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.endswith('.png') or f.endswith('.jpg')]
    # Sort the image files based on their names
    image_files.sort()
    # Load each image file, resize, normalize, and concatenate them into a single numpy array
    image_data = []
    for image_file in image_files:
        image_path = os.path.join(input_folder, image_file)
        image = Image.open(image_path)
        image = image.resize(target_size) # Resize the image
        image_array = np.array(image) / 255.0  # Normalize to range [0, 1]
        image_data.append(image_array)

    # Convert the list of arrays into a single numpy array
    np_data = np.array(image_data)
    print(np_data.shape)
    # Save the numpy array to the output .npy file
    np.save(output_file, np_data)

if __name__ == "__main__":
    # Parse command-line arguments
    cfg = Cfg()
    args = cfg.parse_args()

    # Extract input folder and output file name
    input_folder = args.input_path
    output_file = args.output_path

    # Convert PNG files to a single .npy file
    convert_png_to_npy(input_folder, output_file)

