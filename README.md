## Image Overlay Script

## Description
This Python script overlays a predefined shirt image onto an input image and saves the result as an output image. The script ensures that the input and output files have valid and matching formats before processing.

## Requirements
- Python 3
- Pillow (PIL) library

## Installation
Ensure you have Python installed. Then, install the required dependencies using:
pip install Pillow


## Usage
Run the script with the following command:
python script.py input_image output_image


### Arguments
- `input_image`: Path to the input image (must be `.jpg`, `.jpeg`, or `.png`).
- `output_image`: Path to save the output image (must match the input format).

### Example
python script.py person.jpg output.png


## Error Handling
The script handles the following errors:
- **Incorrect argument count**: If the user does not provide exactly two arguments.
- **Invalid file format**: If the input/output file extensions are not `.jpg`, `.jpeg`, or `.png`.
- **Mismatched file formats**: If the input and output file extensions do not match.
- **File not found**: If the input file does not exist.
- **Unexpected errors**: Any other runtime errors.

## How It Works
1. Checks if the correct number of arguments is provided.
2. Validates the file extensions.
3. Loads `shirt.png` and the input image.
4. Resizes and fits the input image to match the shirt size.
5. Overlays the shirt onto the input image.
6. Saves the final image to the specified output file.

## Notes
- The script requires `shirt.png` to be in the same directory.
- Ensure the input image is large enough for proper resizing.

## License
This project is free to use and modify.

