import json
import numpy as np
import tifffile as tiff
import argparse
import pathlib

def parse_arguments():
    """
    Get the arguments.
    """

    parser = argparse.ArgumentParser(
        description="Split given TIF files into tiles",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("-f", "--filepath", type=str, default="cwd", 
                        required=False, metavar="",
                        help="path to the .tif files to be tiled.")
    parser.add_argument("-c", "--channels", type=str, default="default", 
                        required=False, metavar="",
                        help="Specify path to a JSON file with the markers, \
                        where the key is the channel and the \
                            value the marker name")
    args = parser.parse_args()

    return args.filepath, args.channels

def write_file(image_name, metainf):
    """write the image and metadata to the specified location

    Args:
        image_name (str): 
            name of the image, to which meta information is supposed to be added.
        outpath (str): 
            path where the tiles are supposed to be written 
        metainf (dict(channel_nr: channel_name)): 
            Dictionary containing the information about the channels 
            
    """

    image = tiff.imread(image_name)

    tiff.imwrite(image_name, 
                        image,
                        description=json.dumps(metainf))
       

if __name__ == '__main__':

    # Get the arguments
    filepath, channels = parse_arguments()
    # make path objects out of the strings
    if filepath == "cwd":
        filepath = pathlib.Path.cwd()
    filepath = pathlib.Path(filepath)

    # open the JSON file with the channel info
    with open(channels) as json_file:
        metainf = json.load(json_file)


    # check, if filepath is a folder of tifs or an individual image
    if filepath.is_dir():
        for image in filepath.iterdir():
            if image.suffix == ".tif" or \
            image.suffix == ".tiff":
                write_file(image, metainf)
    
    # else, the path leads to an image
    else:
        image = filepath
        write_file(image, metainf)

         