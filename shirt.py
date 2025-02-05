from os.path import splitext
import sys
from PIL import Image, ImageOps

def main():
    check_arg_count()  # Check if the number of arguments is correct
    check_arg_validity()  # Check if the file extensions are valid

    try:
        # Open the required images and store them in variables
        shirt = Image.open("shirt.png")
        input_image = Image.open(sys.argv[1])
        size = shirt.size
        muppet = ImageOps.fit(input_image, size)
        muppet.paste(shirt, shirt)
        muppet.save(sys.argv[2])
       

    except FileNotFoundError:
        sys.exit("Input file does not exist")
    except Exception as e:
        sys.exit(f"An unexpected error occurred: {e}")

def file_check(file_extension):
    valid_formats = [".jpg", ".jpeg", ".png"]
    return file_extension.lower() in valid_formats

def check_arg_count():
    if len(sys.argv) != 3:
        sys.exit("Usage: python script.py input_image output_image")

def check_arg_validity():
    input_file_ext = splitext(sys.argv[1])[1]
    output_file_ext = splitext(sys.argv[2])[1]

    if not file_check(input_file_ext):
        sys.exit("Invalid input file format")
    if not file_check(output_file_ext):
        sys.exit("Invalid output file format")

    if input_file_ext.lower() != output_file_ext.lower():
        sys.exit("Input and output file formats must be the same")

if __name__ == "__main__":
    main()