# PNG-to-TIFF Conversion Tool

## Overview

This Python script provides a convenient way to collect PNG images from multiple folders and combine them into a single, compressed TIFF file. It's perfect for situations where you need to work with multiple image files in a format suitable for scientific or technical applications.

## Dependencies

- `os` (built-in Python module)
- `PIL` (Pillow): Install with `pip install Pillow`
- `tifffile`: Install with `pip install tifffile`

## Usage

1. Clone or download this repository.
2. Modify the `folder_list` variable in the script to specify the folders containing your PNG images.
3. Run the script from your terminal: `python your_script_name.py`

The script will:

- Search the specified folders for PNG files.
- Attempt to open each PNG image.
- Combine valid PNG images into a multi-page TIFF file named "Result.tif".
- Provide feedback on any errors encountered.
