from PIL import Image, ImageOps
from os.path import splitext
import sys

def main():
    check_cma()
    # Open the input image from the command-line argument
    try:
        input_image = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File does not exist")
    # Open the shirt image
    shirt = Image.open("shirt.png")
    # Save size in a variable (shirt.size returns a tuple like (600,600))
    size = shirt.size
    # Resize the input image to be the same as the shirt image
    input_image_resized = ImageOps.fit(input_image, size)
    # Paste shirt image into input image
    input_image_resized.paste(shirt, shirt)
    # Save formatted image in new file
    input_image_resized.save(sys.argv[2])


def check_cma():
    """Check command-line argument for valid input"""
    # Check if exactly 2 command-line arguments are given
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    # Split extension from file name of the two command-line arguments and return them as list
    extension_1 = splitext(sys.argv[1])
    extension_2 = splitext(sys.argv[2])
    # Check if the 2 given extensions are valid
    if check_extension(extension_1[1]) == False or check_extension(extension_2[1]) == False:
        sys.exit("Invalid input")
    # Check if the 2 given extensions are the same
    if extension_1[1].lower() != extension_2[1].lower():
        sys.exit("Input and output have different extensions")


def check_extension(extension):
    """Check for valid extension type"""
    if extension in [".jpg", ".jpeg", ".png"]:
        return True
    return False


if __name__ == "__main__":
    main()
